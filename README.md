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
- Support sequence split across multiple lines
- Calculate sequence length statistics (min, max, total, average)
- Count unknown bases (N)
- Compute N50 (how fragmented a genome assembly is)
- Unit tested core functions

#### See Phase1Plan.txt for acceptance criteria

---
## Command Line Usage

Genokit is designed as aa command line program with subcommands.

Commands:
- genokit --help: Display help information about the tool and a list of subcommands
- genokit --version: Display the current installed version of Genokit
- genokit fasta-stats filename.fasta: (TODO)Reads a FASTA file and computes basic sequence statistics
