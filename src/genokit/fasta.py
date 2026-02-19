from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FastaRecord:
    id: str
    description: Optional[str]
    sequence: str

    def __post_init__(self):
        if not self.id or not self.id.strip():
            raise ValueError("FASTA record ID cannot be empty")

        if any(ch.isspace() for ch in self.id):
            raise ValueError("FASTA ID cannot contain whitespace")

        if any(ch.isspace() for ch in self.sequence):
            raise ValueError("FASTA record sequence can not contain whitespace")

        if self.sequence != self.sequence.upper():
            raise ValueError("FASTA record sequence must be uppercase")

        if self.description is not None and self.description.strip() == "":
            object.__setattr__(self, "description", None)
