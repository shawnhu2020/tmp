import requests
import time
import random

# List of site URLs to visit
SITE_URL_LIST = [
    "https://www.office.com/",
    "https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage",
    "https://microsoft365.com",
    "https://create.microsoft.com/en-us/template/pacific-presentation-20f81ff3-d0ce-4141-a1ab-c870ef16c9ba",
    "https://facebook.com",
    "https://cisco.com"
]

def generate_traffic():
    while True:
        # Choose a random URL from the list
        url = random.choice(SITE_URL_LIST)
        try:
            # Make a GET request to the selected URL
            response = requests.get(url)
            print(f"Visited {url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to visit {url} - Error: {e}")

        # Wait for a random interval between 5 and 15 seconds
        time.sleep(random.randint(5, 15))

# Run the traffic generator
generate_traffic()
