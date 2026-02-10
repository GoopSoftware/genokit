import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="genokit", description="Genomics toolkit")
    sub = p.add_subparsers(dest="command")
    sub.add_parser("version", help="Show version (placeholder)")
    return p

def main() -> None:
    parser = build_parser()
    parser.parse_args()
