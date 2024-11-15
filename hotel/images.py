from hotel.image import Image
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Images:
    rooms: list[Image] = field(default_factory=list)
    site: list[Image] = field(default_factory=list)
    amenities: list[Image] = field(default_factory=list)
