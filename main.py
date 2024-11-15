import json
from argparse import ArgumentParser
from hotel_data_retriever import HotelDataRetriever

from suppliers.acme_supplier import AcmeSupplier


def main():

  parser = ArgumentParser()

  parser.add_argument("hotel_ids", type=str, help="Hotel IDs")
  parser.add_argument("destination_ids", type=str, help="Destination IDs")

  arguments = parser.parse_args()

  hotel_ids = arguments.hotel_ids.split(",")
  destination_ids = list(map(int, arguments.destination_ids.split(",")))

  result = json.dumps(HotelDataRetriever().get_hotels(hotel_ids,
                                                      destination_ids),
                      indent=4)

  print(result)


if __name__ == "__main__":
  main()
