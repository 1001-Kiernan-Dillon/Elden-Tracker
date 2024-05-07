import requests
import json

# The base URL of the Elden Ring API items endpoint
base_url = 'https://eldenring.fanapis.com/api/items'

# Initialize variables to handle pagination
items = []
total_items = None
page = 0
limit = 100  # You can adjust the limit as needed, up to the maximum allowed by the API

# Loop through all pages and collect items
while total_items is None or len(items) < total_items:
    # Construct the API URL with the current page and limit
    api_url = f'{base_url}?limit={limit}&page={page}'
    
    # Make a GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Update the total_items if it's the first request
        if total_items is None:
            total_items = data['total']
        
        # Extend the items list with the current page's items
        items.extend(data['data'])
        
        # Increment the page number for the next request
        page += 1
    else:
        print(f"Failed to fetch items on page {page}: {response.status_code}")
        break

# Path where you want to save the JSON file
json_file_path = 'C:/Users/kiern/Downloads/all_items.json'

# Save the items to a JSON file
with open(json_file_path, 'w') as file:
    json.dump(items, file, indent=4)

print(f"All items saved to {json_file_path}")
