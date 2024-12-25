import json
from argparse import ArgumentParser
from hotel_data_retriever import HotelDataRetriever

def main():

    parser = ArgumentParser()

    parser.add_argument("hotel_ids", type=str, nargs="?", default = None, help="Hotel IDs")
    parser.add_argument("destination_ids", type=str, nargs="?", default = None, help="Destination IDs")

    arguments = parser.parse_args()

    hotel_ids = arguments.hotel_ids
    destination_ids = arguments.destination_ids

    if hotel_ids is not None:
        hotel_ids = hotel_ids.split(",")

    if destination_ids is not None:
        destination_ids = list(map(int, destination_ids.split(",")))

    result = HotelDataRetriever().get_hotels(hotel_ids, destination_ids)

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
