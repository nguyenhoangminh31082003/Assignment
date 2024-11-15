from hotel.hotel import Hotel
from hotel.image import Image
from hotel.images import Images
from hotel.location import Location
from suppliers.supplier import Supplier


class PatagoniaSupplier(Supplier):

  @staticmethod
  def get_url() -> str:
    return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

  @staticmethod
  def parse_data(raw_data: dict) -> Hotel:

    location = Location(lat=raw_data["lat"],
                        lng=raw_data["lng"],
                        address=raw_data["address"])

    roomImages = PatagoniaSupplier.parse_image_list(
        raw_data["images"]["rooms"])
    amenityImages = PatagoniaSupplier.parse_image_list(
        raw_data["images"]["amenities"])

    images = Images(rooms=roomImages, amenities=amenityImages)

    return Hotel(id=raw_data["id"],
                 destination_id=raw_data["destination"],
                 name=raw_data["name"],
                 description=raw_data["info"],
                 location=location,
                 images=images)

  @staticmethod
  def parse_image_list(raw_images: list[dict]) -> list[Image]:
    return [
        Image(link=image["url"], description=image["description"])
        for image in raw_images
    ]
