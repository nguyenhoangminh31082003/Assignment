from typing import Optional
from dataclasses import dataclass


@dataclass
class Image:
  link: Optional[str] = None
  description: Optional[str] = None
