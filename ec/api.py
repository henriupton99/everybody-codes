import json
import requests
from pathlib import Path

from ec.utils import decrypt, html_to_markdown

SOLUTION_TEMPLATE = '''
def part_1(data: str) -> int | str | None:
    lines = data.splitlines()
    return None  # TODO


def part_2(data: str) -> int | str | None:
    lines = data.splitlines()
    return None  # TODO


def part_3(data: str) -> int | str | None:
    lines = data.splitlines()
    return None  # TODO
'''

class Client:
    site_url = "https://everybody.codes"
    api_url = "https://api.everybody.codes"
    user_agent = "Personal EverybodyCodes client (github: henriupton99)"
    cache_path = Path(".session.json")

    def __init__(self):
        self.cache = self._load_cache()
        if "session_cookie" not in self.cache:
            self.cache["session_cookie"] = input("Please paste session cookie: ").strip()
            self._save_cache()

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": self.user_agent,
            "Cookie": f"everybody-codes={self.cache['session_cookie']}",
        })

        if "seed" not in self.cache:
            self.cache["seed"] = int(self._get_json(f"{self.api_url}/user/me")["seed"])
            self._save_cache()
        self.seed = self.cache["seed"]

    def _load_cache(self) -> dict:
        if self.cache_path.exists():
            return json.loads(self.cache_path.read_text())
        return {}

    def _save_cache(self) -> None:
        self.cache_path.write_text(json.dumps(self.cache, indent=2))

    def _get_json(self, url: str) -> dict:
        r = self.session.get(url, timeout=15)
        if r.status_code != 200:
            raise ValueError(f"HTTP {r.status_code} sur {url}")
        if "json" not in r.headers.get("Content-Type", "") and r.text.lstrip().startswith("<"):
            raise ValueError(f"{url} a renvoyé du HTML, pas du JSON (mauvaise route ou quête pas ouverte)")
        return r.json()
    
    def _quest_dir(self, event, quest) -> Path:
        d = Path(f"assets/{event}/quest_{int(quest):02d}")
        d.mkdir(exist_ok=True, parents=True)
        return d

    @staticmethod
    def quest_dir(event, quest) -> Path:
        return Path("assets") / str(event) / f"quest_{int(quest):02d}"

    def fetch(self, event, quest, part) -> Path:
        part = str(part)
        d = self.quest_dir(event, quest)

        key = self._get_json(f"{self.api_url}/event/{event}/quest/{quest}").get(f"key{part}")
        if not key:
            raise ValueError(f"Clé absente pour la partie {part} (pas encore débloquée ?)")

        d.mkdir(parents=True, exist_ok=True)

        inputs = self._get_json(f"{self.site_url}/assets/{event}/{quest}/input/{self.seed}.json")
        (d / f"input_part{part}.txt").write_text(decrypt(hex_text=inputs[part], key=key), encoding="utf-8")

        descs = self._get_json(f"{self.site_url}/assets/{event}/{quest}/description.json")
        md = html_to_markdown(decrypt(hex_text=descs[part], key=key))
        (d / f"desc_part{part}.md").write_text(md, encoding="utf-8")

        solution = d / "solution.py"
        if not solution.exists():
            solution.write_text(SOLUTION_TEMPLATE.format(event=event, quest=int(quest)), encoding="utf-8")
            print(f"📝 Template créé : {solution}")

        print(f"✅ Partie {part} récupérée dans {d}")
        return d

    def submit(self, event, quest, part, answer) -> dict:
        url = f"{self.api_url}/event/{event}/quest/{quest}/part/{part}/answer"
        r = self.session.post(url, json={"answer": str(answer)}, timeout=15)

        if r.status_code == 409:
            print("ℹ️ Partie déjà résolue.")
        elif r.status_code == 423:
            print("⏳ Verrouillé : mauvaise réponse trop récente, attends un peu.")
        elif r.status_code != 200:
            print(f"❌ HTTP {r.status_code} : {r.text[:200]}")
        else:
            result = r.json()
            print("🎉 CORRECT" if result.get("correct") else "💥 Incorrect")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return result
        return {"status": r.status_code, "body": r.text}
        
        
        
