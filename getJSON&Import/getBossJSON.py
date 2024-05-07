import requests
import json

# The base URL of the Elden Ring API bosses endpoint
base_url = 'https://eldenring.fanapis.com/api/bosses'

# Initialize variables to handle pagination
bosses = []
total_bosses = None
page = 0
limit = 100  # You can adjust the limit as needed, up to the maximum allowed by the API

# Loop through all pages and collect bosses
while total_bosses is None or len(bosses) < total_bosses:
    # Construct the API URL with the current page and limit
    api_url = f'{base_url}?limit={limit}&page={page}'
    
    # Make a GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Update the total_bosses if it's the first request
        if total_bosses is None:
            total_bosses = data['total']
        
        # Process each boss and handle "???" in healthPoints
        for boss in data['data']:
            health_points = boss.get('healthPoints', None)  # Use .get() with a default value of None
            if health_points == "???":
                health_points = None  # Replace "???" with None
            boss['healthPoints'] = health_points  # Update the boss entry
            bosses.append(boss)
        
        # Increment the page number for the next request
        page += 1
    else:
        print(f"Failed to fetch bosses on page {page}: {response.status_code}")
        break

# Path where you want to save the JSON file
json_file_path = 'C:/Users/kiern/Downloads/all_bosses.json'

# Save the bosses to a JSON file
with open(json_file_path, 'w') as file:
    json.dump(bosses, file, indent=4)

print(f"All bosses saved to {json_file_path}")
