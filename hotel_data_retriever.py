from typing import Optional
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

        self.hotels = self._retrieve_and_merge_data()

    def _retrieve_and_merge_data(self) -> list[dict]:
        hotels = {}

        for supplier in self.suppliers:

            for hotel in supplier.get_parsed_data():
                key = (hotel.id, hotel.destination_id)
                if key in hotels:
                    hotels[key] = HotelMerger.merge_hotel_record(hotels[key], hotel)
                else:
                    hotels[key] = hotel

        return [asdict(hotel) for hotel in hotels.values()] 

    def get_hotels(self, hotel_ids: Optional[list[str]], destination_ids: Optional[list[int]]) -> list[dict]:

        if (hotel_ids is None) and (destination_ids is None):
            return [hotel for hotel in self.hotels]
        
        if hotel_ids is None:
            destination_ids = set(destination_ids)
            return [hotel for hotel in self.hotels if hotel["destination_id"] in destination_ids]
        
        if destination_ids is None:
            hotel_ids = set(hotel_ids)
            return [hotel for hotel in self.hotels if hotel["id"] in hotel_ids]

        hotel_ids = set(hotel_ids)
        destination_ids = set(destination_ids)

        return [hotel for hotel in self.hotels if hotel["id"] in hotel_ids and hotel["destination_id"] in destination_ids]
