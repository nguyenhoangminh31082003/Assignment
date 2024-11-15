from typing import Optional
from hotel.hotel import Hotel
from hotel.location import Location
from hotel.amenities import Amenities
from hotel.images import Images
from hotel.image import Image

class HotelMerger:

    @staticmethod
    def merge_and_deduplicate_lists(a: list[str], b: list[str]) -> list[str]:
        return list(set(a) | set(b))

    @staticmethod
    def choose_more_specific_string(a: Optional[str], b: Optional[str]) -> Optional[str]:
        if not a:
            return b
        if not b:
            return a
        return a if len(a) > len(b) else b

    @classmethod
    def merge_location(cls, a: Location, b: Location) -> Location:
        return Location(
            lat=a.lat or b.lat,
            lng=a.lng or b.lng,
            address=cls.choose_more_specific_string(a.address, b.address),
            city=cls.choose_more_specific_string(a.city, b.city),
            country=cls.choose_more_specific_string(a.country, b.country)
        )
    
    @classmethod
    def merge_amenities(cls, a: Amenities, b: Amenities) -> Amenities:
        return Amenities(
            general=cls.merge_and_deduplicate_lists(a.general, b.general),
            room=cls.merge_and_deduplicate_lists(a.room, b.room)
        )
    
    @classmethod
    def merge_image_list(cls, a: list[Image], b: list[Image]) -> list[Image]:
        images = {}
        for image in a:
            images[image.link] = image.description
        for image in b:
            if image.link not in images:
                images[image.link] = image.description
            else:
                images[image.link] = cls.choose_more_specific_string(images[image.link], image.description)
        return [Image(link=link, description=description) for link, description in images.items()]

    @classmethod
    def merge_images(cls, a: Images, b: Images) -> Images:
        return Images(
            rooms=cls.merge_image_list(a.rooms, b.rooms),
            site=cls.merge_image_list(a.site, b.site),
            amenities=cls.merge_image_list(a.amenities, b.amenities)
        )

    @classmethod
    def merge_hotel_record(cls, a: Hotel, b: Hotel) -> Hotel:
        if (a.id != b.id) or (a.destination_id != b.destination_id):
            raise ValueError("Only records referring to the same hotel can be merged")

        return Hotel(
            id=a.id,
            destination_id=b.destination_id,
            name=cls.choose_more_specific_string(a.name, b.name),
            description=cls.choose_more_specific_string(a.description, b.description),
            location=cls.merge_location(a.location, b.location),
            amenities=cls.merge_amenities(a.amenities, b.amenities),
            images=cls.merge_images(a.images, b.images),
            booking_conditions=cls.merge_and_deduplicate_lists(a.booking_conditions, b.booking_conditions)
        )
