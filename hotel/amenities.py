from dataclasses import dataclass, field


@dataclass(frozen=True)
class Amenities:
    general: list[str] = field(default_factory=list)
    room: list[str] = field(default_factory=list)
