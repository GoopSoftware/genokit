# Genokit A Minimal Genomics Command Line Toolkit
A lightweight python CLI toolkit for working with DNA sequence 
files such as FASTA and FASTQ.

This project focuses on building clean, well tested software for 
reading DNA data files and computing simple statistics about the 
sequences they contain.

The goal is to understand how genomic data is structured and how 
researchers evaluate basic properties of DNA sequence data.
---

## Current Phase: 1

### Phase 1 Sequence I/O + basic stats for FASTA
In phase 1, the tool reads a FASTA file and calculates simple statistics about the DNA sequences inside of them.

Planned features:

- Read FASTA files containing one or more DNA sequences
- Support sequence split accross multiple lines
- Calculate sequence length statistics (min, max, total, average)
- Count unknown bases (N)
- Compute N50 (how fragmented a genome assembly is)
- Unit tested core functions

#### See Phase1Plan.txt for acceptance criteria

---

#### Why this matters in Genomics?
When scientists sequence DNA, they often end up with many fragments rather than one perfect sequence. Before doing deeper analysis they check
- How long the fragments are
- Whether the base composition looks normal
- How fragmented the assembly is
- How many bases could not be determined

This tool implements those checks from scratch in order to understand how real genomic data is evaluated

---


