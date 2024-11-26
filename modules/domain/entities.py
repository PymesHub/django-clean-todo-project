from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: Optional[str]
    completed: bool = False