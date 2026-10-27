import argparse
import sys

from ec.api import Client
from ec.runner import run_part


def cmd_fetch(args):
    Client().fetch(args.event, args.quest, args.part)


def cmd_run(args):
    answer, elapsed = run_part(Client.quest_dir(args.event, args.quest), args.part)
    print(f"Partie {args.part} : {answer}   ({elapsed * 1000:.1f} ms)")
    return answer


def cmd_submit(args):
    answer = args.answer if args.answer is not None else cmd_run(args)

    if not args.yes:
        confirm = input(f"Soumettre « {answer} » pour la partie {args.part} ? [o/N] ")
        if confirm.strip().lower() not in ("o", "y"):
            print("Annulé.")
            return

    client = Client()
    result = client.submit(args.event, args.quest, args.part, answer)

    if result.get("correct") and args.part < 3:
        print("🔓 Récupération de la partie suivante…")
        client.fetch(args.event, args.quest, args.part + 1)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ec", description="Client Everybody Codes")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name, func, help_ in (
        ("fetch", cmd_fetch, "récupère input + énoncé (crée solution.py au premier fetch)"),
        ("run", cmd_run, "exécute part_N sur l'input réel"),
        ("submit", cmd_submit, "exécute part_N puis soumet la réponse"),
    ):
        sp = sub.add_parser(name, help=help_)
        sp.add_argument("event", type=int, help="ex. 2025")
        sp.add_argument("quest", type=int, help="ex. 1")
        sp.add_argument("part", type=int, choices=(1, 2, 3))
        sp.set_defaults(func=func)
        if name == "submit":
            sp.add_argument("-a", "--answer", help="réponse manuelle (sinon calculée)")
            sp.add_argument("-y", "--yes", action="store_true", help="sans confirmation")

    args = parser.parse_args(argv)
    try:
        args.func(args)
    except (ValueError, FileNotFoundError) as exc:
        sys.exit(f"❌ {exc}")


if __name__ == "__main__":
    main()
