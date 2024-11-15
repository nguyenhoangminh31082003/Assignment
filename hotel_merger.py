from typing import Optional
from hotel.hotel import Hotel

class HotelMerger:

    @classmethod
    def merge_hotel_record(a: Hotel, b: Hotel) -> Hotel:
        assert (a.id == b.id) and (a.destination_id == b.destination_id), "Only records refering to the same hotel can be merged"

        return Hotel(id=a.id, 
                    destination_id=b.destination_id)