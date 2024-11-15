from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Image:
    link: Optional[str] = None
    description: Optional[str] = None
