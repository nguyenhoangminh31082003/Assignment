# Assignment

This application is a CLI-based tool designed to fetch, clean, and merge hotel data from multiple suppliers, allowing users to retrieve tailored results based on specific input.

## System Overview

The system is composed of three main components:

1. **Fetching and Parsing Component**

This component retrieves raw hotel data from multiple suppliers and standardizes it into a consistent format. It is primarily implemented using classes that inherit from the `Supplier` class, allowing for extensibility and supplier-specific data handling.

2. **Merging Component**

This component defines strategies for selecting the most appropriate data to merge attributes of the same hotels from various sources into a unified representation. The `HotelMerger` class serves as the primary implementation of this functionality.

3. **Retrieving Component**

This component provides a filtered list of hotels based on user-specified hotel IDs and destination IDs. It is primarily implemented through the `HotelDataRetriever` class.
