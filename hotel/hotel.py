from typing import Optional
from hotel.images import Images
from hotel.location import Location
from hotel.amenities import Amenities
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Hotel:
    id: str
    destination_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    location: Location = field(default_factory=Location)
    amenities: Amenities = field(default_factory=Amenities)
    images: Images = field(default_factory=Images)
    booking_conditions: list[str] = field(default_factory=list)
