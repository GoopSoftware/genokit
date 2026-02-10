from genokit.cli import main


def test_import_genokit():
    import genokit  # noqa: F401


def test_help_returns_zero(capsys):
    code = main(["--help"])
    assert code == 0
    out = capsys.readouterr().out
    assert "genokit" in out
    assert "fasta-stats" in out


def test_fasta_stats_placeholder(capsys):
    code = main(["fasta-stats", "dummy.fasta"])
    assert code == 0
    assert capsys.readouterr().out.strip() == "TODO"
