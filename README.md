# genokit
Genomics toolkit (CLI + tests).


# Phase 1


## Acceptance Criteria 1
Expectation:
Should be able to point this tool at a FASTA file from NCBI, Ensembl or a lab and it should work

Acceptance Criteria
- Load any normal FASTA file and trust the output
- Supports multiple sequences
- Supports blank lines
- support lowercase bases

Test: If I download a FASTA from the internet and run the parser, I get correct sequences without manual cleanup

---
## Acceptance Criteria 2
Expectation:
Once data is parsed I dont want to have to think about FASTA quirks ever again

Acceptance Criteria
- id is stable and usable as a key
- description is preserved if present
- sequence is
  - uppercase
  - contains no whitespace
  - ready for length / GC / motif analysis

Case: sequence before the header
Test: I can do len(record.sequence) or record.sequence.count("G") without worrying about spaces, newlines, or lowercase

---
## Acceptance Criteria 3
Expectation:
If the file is malformed I want to know immediately and not get wrong results

Acceptance Criteria
- If data starts before a >, stop
- Raises ValueError
- Message clearly explains what is wrong

Test: If I pass a broken file the program will refuse to run


---
## Acceptance Criteria 4
Expectation: Weird but legitimate FASTA files shouldn't break the program

Acceptance Criteria
- Record exists
- sequence == ""
- No crash

Case: header with no sequence
Test: Pipeline continues running and I can decide how to handle empty sequences later

---
## Acceptance Criteria 5
Expectation
This shouldnt load a 3gb genome into memory all at once

Acceptance Criteria
- parse_fasta() should be an iterator/generator
- Records are yielded one by one

test: Can loop parse_fasta("genome.fa"):

---
## Acceptance Criteria 6
Expectation
Before trusting stats I want proof that the file is being read correctly

Acceptance criteria
- genokit gasta-stats file.fasta
  - successfully loads file
  - prints
    - number of records
    - first record id
    - first record length

Test: I can immediately see whether the file was parsed correctly