import requests
import json

def fetch_and_save_json(api_url, output_filename="output.json"):
    """
    Fetch data from an API and save it to a JSON file.
    
    Parameters:
    - api_url (str): API endpoint URL
    - output_filename (str): Name of the file to save JSON data
    
    Returns:
    - dict or list: JSON data fetched from API
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an error for HTTP errors (4xx, 5xx)

        data = response.json()  # Convert response to JSON

        with open(output_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return data  # Return data for testing purposes

    except requests.exceptions.RequestException as e:
        print(f"Error fetching API: {e}")
        return None  # Return None in case of an error

# Run script manually to fetch API data
if __name__ == "__main__":
    API_URL = "https://api.nationalize.io/?name=nathaniel"  # Sample API
    fetch_and_save_json(API_URL)