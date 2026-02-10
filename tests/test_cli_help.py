from genokit.cli import build_parser

def test_help_builds():
    parser = build_parser()
    assert parser.prog == "genokit"
