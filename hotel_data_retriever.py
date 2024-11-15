from hotel.hotel import Hotel
from suppliers.acme_supplier import AcmeSupplier
from suppliers.patagonia_supplier import PatagoniaSupplier
from suppliers.paperflies_supplier import PaperfliesSupplier


class HotelDataRetriever:

  def __init__(self):
    self.suppliers = [
        AcmeSupplier(),
        PatagoniaSupplier(),
        PaperfliesSupplier()
    ]

  @staticmethod
  def merge_hotel_record(a: Hotel, b: Hotel) -> Hotel:
    assert (a.id == b.id) and (
        a.destination_id == b.destination_id
    ), "Only records refering to the same hotel can be merged"

    return Hotel(a.id, b.destination_id)

  def get_hotels(self, hotel_ids: list[str],
                 destination_ids: list[int]) -> list[dict]:
    return []
