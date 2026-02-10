import argparse
from genokit import __version__

def cmd_fasta_stats(args: argparse.Namespace) -> int:
    print("TODO")
    return 0

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="genokit", description="Genomics toolkit")

    parser.add_argument(
        "--version",
        action="version",
        version="genokit " + __version__,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    fasta = subparsers.add_parser("fasta-stats", help="Placeholder FASTA stats command")
    fasta.add_argument("path", help="Path to FASTA file (not read yet)")


    return parser

def main(argv=None):
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 0

    if args.command == "fasta-stats":
        print("TODO")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())