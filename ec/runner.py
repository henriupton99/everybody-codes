import importlib.util
import time
from pathlib import Path


def load_solution(quest_dir: Path):
    path = quest_dir / "solution.py"
    if not path.exists():
        raise FileNotFoundError(f"{path} absent : lance d'abord `fetch`.")
    name = f"solution_{quest_dir.parent.name}_{quest_dir.name}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_part(quest_dir: Path, part: int):
    """Exécute part_N sur l'input réel. Renvoie (réponse, durée en secondes)."""
    input_path = quest_dir / f"input_part{part}.txt"
    if not input_path.exists():
        raise FileNotFoundError(f"{input_path} absent : partie {part} pas encore récupérée.")

    func = getattr(load_solution(quest_dir), f"part_{part}")
    data = input_path.read_text(encoding="utf-8").rstrip("\n")

    start = time.perf_counter()
    answer = func(data)
    elapsed = time.perf_counter() - start

    if answer is None:
        raise ValueError(f"part_{part} renvoie None : pas encore implémentée ?")
    return answer, elapsed
