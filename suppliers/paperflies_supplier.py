from hotel.amenities import Amenities
from hotel.hotel import Hotel
from hotel.image import Image
from hotel.images import Images
from hotel.location import Location
from suppliers.supplier import Supplier


class PaperfliesSupplier(Supplier):

    @staticmethod
    def get_url() -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    @staticmethod
    def parse_data(raw_data: dict) -> Hotel:

        location = Location(address=raw_data["location"]["address"],
                            country=raw_data["location"]["country"])

        amenties = Amenities(general=raw_data["amenities"]["general"],
                             room=raw_data["amenities"]["room"])

        roomImages = PaperfliesSupplier.parse_image_list(raw_data["images"]["rooms"])
        siteImages = PaperfliesSupplier.parse_image_list(raw_data["images"]["site"])

        images = Images(rooms=roomImages, site=siteImages)

        return Hotel(id=raw_data["hotel_id"],
                     destination_id=raw_data["destination_id"],
                     name=raw_data["hotel_name"],
                     description=raw_data["details"],
                     location=location,
                     amenities=amenties,
                     images=images,
                     booking_conditions=raw_data["booking_conditions"])

    @staticmethod
    def parse_image_list(raw_images: list[dict]) -> list[Image]:
        return [Image(link=image["link"], description=image["caption"]) for image in raw_images]
