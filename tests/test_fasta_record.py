import pytest
from genokit.fasta import FastaRecord


def test_valid_record_created():
    r = FastaRecord(id="seq1", description="description", sequence="ATGCGTACGTTAGCTAGCTAGCTA")
    assert r.id == "seq1"
    assert r.description == "description"
    assert r.sequence == "ATGCGTACGTTAGCTAGCTAGCTA"


def test_empty_description_becomes_none():
    r = FastaRecord(id="seq1", description="", sequence="ATGC")
    assert r.description is None


def test_whitespace_description_becomes_none():
    r = FastaRecord(id="seq1", description=" ", sequence="ATGC")
    assert r.description is None


def test_record_allows_empty_sequence():
    r = FastaRecord(id="seq1", description=None, sequence="")
    assert r.sequence == ""


def test_rejects_empty_id():
    with pytest.raises(ValueError):
        FastaRecord(id="", description=None, sequence="ATGC")


def test_rejects_whitespace_id():
    with pytest.raises(ValueError):
        FastaRecord(id="  ", description=None, sequence="ATGC")


def test_rejects_contains_whitespace_id():
    with pytest.raises(ValueError):
        FastaRecord(id="a  a", description=None, sequence="ATGC")


def test_rejects_sequence_with_whitespace():
    with pytest.raises(ValueError):
        FastaRecord(id="seq1", description=None, sequence=" ATGCGTA CGTTAGC TAGCTA GCTA ")


def test_rejects_lowercase_sequence():
    with pytest.raises(ValueError):
        FastaRecord(id="seq1", description=None, sequence="atgcgtacgttagctagctagcta")


def test_rejects_mixed_upperlowercase_sequence():
    with pytest.raises(ValueError):
        FastaRecord(id="seq1", description=None, sequence="ATGCGTACGttagctagctagcta")