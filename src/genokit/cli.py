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
    fasta.set_defaults(func=cmd_fasta_stats)

    return parser

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())