import datetime
from tabulate import tabulate

# Simulated flight records (In a real-world scenario, this would come from a database)
flights = [
    {"name": "John Doe", "flight_number": "AA123", "date": "2024-10-01", "destination": "New York"},
    {"name": "Jane Smith", "flight_number": "DL456", "date": "2024-10-05", "destination": "Los Angeles"},
    {"name": "John Doe", "flight_number": "UA789", "date": "2024-10-10", "destination": "Chicago"},
    {"name": "Alice Brown", "flight_number": "AA101", "date": "2024-10-15", "destination": "San Francisco"}
]


def get_user_input():
    """Prompt the user for their details."""
    print("Please provide the following details to verify if you've been on a flight:")
    name = input("Full Name: ")
    flight_number = input("Flight Number (optional, press enter to skip): ").strip()
    date_input = input("Date of flight (YYYY-MM-DD, optional, press enter to skip): ").strip()

    # Validate date format if provided
    if date_input and not validate_date(date_input):
        print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")
        return None, None, None

    return name, flight_number, date_input


def validate_date(date_str):
    """Check if the provided date string is in the correct format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def check_flight_history(name, flight_number=None, date=None):
    """Check if the user has been on a flight based on provided criteria."""
    matching_flights = []

    for flight in flights:
        # Match by name, and optionally by flight number and date
        if flight["name"].lower() == name.lower():
            if flight_number and flight["flight_number"].lower() != flight_number.lower():
                continue  # Skip if the flight number doesn't match
            if date and flight["date"] != date:
                continue  # Skip if the date doesn't match
            matching_flights.append(flight)

    return matching_flights


def display_flight_history(flights_found):
    """Display flight history in a table format."""
    table = [[f["flight_number"], f["date"], f["destination"]] for f in flights_found]
    print(tabulate(table, headers=["Flight Number", "Date", "Destination"], tablefmt="grid"))


def main():
    while True:
        name, flight_number, date = get_user_input()

        if name is None:
            print("Name is required. Please try again.")
            continue  # Prompt again for valid input

        # Check if the user has been on any flight
        flights_found = check_flight_history(name, flight_number, date)

        if flights_found:
            print("\nFlight History for", name)
            display_flight_history(flights_found)
        else:
            print(f"\nNo flight records found for {name} based on the provided information.")
        break


# Run the script
if __name__ == "__main__":
    main()
