## FASTA Parser – Test Cases

| Precondition | Action | Expected Result | Notes |
|--------------|--------|----------------|-------|
| ID with white space | Parse | ID = first token<br>Description = everything after first space | There really is no way to actually know if an ID contains whitespace because standard for fasta is `>(id) (description)`. If we find a way to detect whitespace in an ID update this |
| Blank lines before `>` | Ignore blank lines until `>` is found then parse | Ignored whitespace | Some files may have empty lines before `>` these are valid |
| Valid ID | Continue with parsing | Parse fasta data | Fasta standards mark all characters as valid for ID |
| Empty description | Parse file with None description | Description = None | Empty descriptions are common so we will need to allow empty descriptions. For safety convert to None. This will allow for easier logic later |
| Sequence split across 2 or more lines | Concatenate with no new lines | — | — |
| Fasta with whitespace<br>`TTA  CTAA TGAG  CTG` | Strip whitespace | `TTACTAATGAGCTG` | — |
| Fasta with lowercase<br>`ttactaatgagctg` | Convert to uppercase | `TTACTAATGAGCTG` | While iterating through the record convert to upper() |
| Fasta file with multiple sequences<br>`>seq1 some description`<br>`ACGT`<br>`>seq2 some description`<br>`GGGG`<br>`>seq3 some description` | Create a list of sequences | `len(records == 3)` | Acceptance criteria 1 |