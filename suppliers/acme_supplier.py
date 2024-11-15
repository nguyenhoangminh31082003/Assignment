from hotel.hotel import Hotel
from hotel.location import Location
from suppliers.supplier import Supplier


class AcmeSupplier(Supplier):

  @staticmethod
  def get_url() -> str:
    return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

  @staticmethod
  def parse_data(raw_data: dict) -> Hotel:

    location = Location(lat=raw_data["Latitude"],
                        lng=raw_data["Longitude"],
                        address=raw_data["Address"],
                        city=raw_data["City"],
                        country=raw_data["Country"])

    return Hotel(id=raw_data["Id"],
                 destination_id=raw_data["DestinationId"],
                 name=raw_data["Name"],
                 description=raw_data["Description"],
                 location=location)
