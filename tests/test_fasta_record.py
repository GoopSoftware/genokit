import pytest

from genokit.fasta import FastaRecord

def test_record_allows_empty_sequence():
    r = FastaRecord(id="seq1", description=None, sequence="")
    assert r.id == "seq1"
    assert r.sequence == ""

