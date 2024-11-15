from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    lat: Optional[float] = None
    lng: Optional[float] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
