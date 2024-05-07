import requests
import json

# The base URL of the Elden Ring API talismans endpoint
base_url = 'https://eldenring.fanapis.com/api/talismans'

# Initialize variables to handle pagination
talismans = []
total_talismans = None
page = 0
limit = 100  # You can adjust the limit as needed, up to the maximum allowed by the API

# Loop through all pages and collect talismans
while total_talismans is None or len(talismans) < total_talismans:
    # Construct the API URL with the current page and limit
    api_url = f'{base_url}?limit={limit}&page={page}'
    
    # Make a GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Update the total_talismans if it's the first request
        if total_talismans is None:
            total_talismans = data['total']
        
        # Extend the talismans list with the current page's talismans
        talismans.extend(data['data'])
        
        # Increment the page number for the next request
        page += 1
    else:
        print(f"Failed to fetch talismans on page {page}: {response.status_code}")
        break

# Path where you want to save the JSON file
json_file_path = 'C:/Users/kiern/Downloads/all_talismans.json'

# Save the talismans to a JSON file
with open(json_file_path, 'w') as file:
    json.dump(talismans, file, indent=4)

print(f"All talismans saved to {json_file_path}")
