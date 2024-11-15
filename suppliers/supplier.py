import requests
from hotel.hotel import Hotel
from abc import ABC, abstractmethod

class Supplier(ABC):

    @staticmethod
    @abstractmethod
    def get_url() -> str:
        pass

    def fetch_raw_data(self) -> list[dict]:
        url = self.get_url()
        response = requests.get(url)
        return response.json()

    @staticmethod
    @abstractmethod
    def parse_data(raw_data: dict) -> Hotel:
        pass

    def get_parsed_data(self) -> list[Hotel]:
        raw_data = self.fetch_raw_data()
        return [self.parse_data(hotel) for hotel in raw_data]
