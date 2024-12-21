import requests
from requests.exceptions import RequestException
from urllib3.exceptions import IncompleteRead

class CountryInfo:
    # Constructor to initialize the URL
    def __init__(self, url):
        self.url = url

    # Method to fetch and return country data (only one attempt)
    def fetch_data(self):
        try:
            # Set timeout to 10 seconds
            response = requests.get(self.url, timeout=10)  
            response.raise_for_status()  
            return response.json()  
        except IncompleteRead as e:
            print(f"Error fetching data: Incomplete Read - {e}")
            return None
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    # Method to display countries using a specific currency
    def countries_using_currency(self, currency_input):
        data = self.fetch_data()
        if data is None:
            return  # Stop if data fetch fails

        # Normalize input currency (lowercase)
        if currency_input == "dollar":
            target_currency = "united states dollar"
        elif currency_input == "euro":
            target_currency = "euro"
        else:
            print("Please enter 'dollar' or 'euro'.")
            return

        # Check each country for the target currency
        found = False
        print(f"\nCountries using {currency_input.capitalize()} as currency:")
        for country in data:
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                if target_currency.lower() in currency_info.get('name', '').lower():
                    print(country.get('name', {}).get('common', 'N/A'))
                    found = True

        if not found:
            print(f"No countries found using {currency_input.capitalize()} as currency.")

    # Method to display all countries with their currencies and symbols
    def display_all_countries(self):
        data = self.fetch_data()
        if data is None:
            return  # Stop if data fetch fails

        print(f"\n{'Country Name':<30} {'Currency':<20} {'Currency Symbol'}")
        print("-" * 60)
        for country in data:
            country_name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"{country_name:<30} {currency_name:<20} {currency_symbol}")


# Main Program Execution
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_info = CountryInfo(url)

    # Take user input for which action to perform
    while True:
        print("\nChoose an option:")
        print("1. Display countries using a specific currency (Dollar or Euro)")
        print("2. Display all countries with currencies and symbols")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            # Get user input for currency (either 'dollar' or 'euro')
            currency_input = input("\nEnter the currency you want to search for (dollar or euro): ").strip().lower()
            country_info.countries_using_currency(currency_input)

        elif choice == '2':
            # Display all countries with currencies
            country_info.display_all_countries()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")








import requests

class BreweryInfo:
    def __init__(self, url):
        self.url = url

    # Method to fetch data from the API based on state
    def fetch_breweries_by_state(self, state):
        response = requests.get(f"{self.url}/breweries?by_state={state}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {state}: {response.status_code}")
            return []

    # Method to list the names of all breweries in the selected states
    def list_breweries(self, states):
        for state in states:
            print(f"\nBreweries in {state}:")
            breweries = self.fetch_breweries_by_state(state)
            if not breweries:
                print(f"No breweries found in {state}")
            else:
                for brewery in breweries:
                    print(brewery['name'])

    # Method to count the number of breweries in each state
    def count_breweries(self, states):
        for state in states:
            breweries = self.fetch_breweries_by_state(state)
            print(f"\nNumber of breweries in {state}: {len(breweries)}")

    # Method to count types of breweries in individual cities of the states
    def count_brewery_types_by_city(self, states):
        for state in states:
            print(f"\nBrewery types by city in {state}:")
            breweries = self.fetch_breweries_by_state(state)
            city_brewery_types = {}
            for brewery in breweries:
                city = brewery.get('city', 'Unknown City')
                brewery_type = brewery.get('type', 'Unknown Type')
                if city not in city_brewery_types:
                    city_brewery_types[city] = set()  
                city_brewery_types[city].add(brewery_type)

            # Print the types count per city
            for city, types in city_brewery_types.items():
                print(f"{city}: {len(types)} different types")

    # Method to count breweries with websites in the selected states
    def count_breweries_with_websites(self, states):
        for state in states:
            print(f"\nBreweries with websites in {state}:")
            breweries = self.fetch_breweries_by_state(state)
            count = 0
            for brewery in breweries:
                if brewery.get('website_url'):
                    count += 1
            print(f"Number of breweries with websites in {state}: {count}")

# Main Program Execution
if __name__ == "__main__":
    url = "https://api.openbrewerydb.org"
    brewery_info = BreweryInfo(url)

    # Input from user to select states
    states_input = input("Enter states (separated by commas) to search for breweries: ").strip()
    states = [state.strip() for state in states_input.split(',')]

    # List all breweries in the selected states
    brewery_info.list_breweries(states)

    # Count the number of breweries in each selected state
    brewery_info.count_breweries(states)

    # Count brewery types by city in each selected state
    brewery_info.count_brewery_types_by_city(states)

    # Count and list breweries with websites in each selected state
    brewery_info.count_breweries_with_websites(states)

