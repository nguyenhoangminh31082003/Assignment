from dataclasses import asdict
from hotel_merger import HotelMerger
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

        hotels = {}

        for supplier in self.suppliers:
            for hotel in supplier.get_parsed_data():
                key = (hotel.id, hotel.destination_id)
                hotels[key] = hotel

        self.hotels = [asdict(hotel) for hotel in hotels.values()]     

    def get_hotels(self, hotel_ids: list[str], destination_ids: list[int]) -> list[dict]:
        return [hotel for hotel in self.hotels if hotel['id'] in hotel_ids and hotel['destination_id'] in destination_ids]
