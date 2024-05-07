import json
import psycopg2
from psycopg2 import extras

# Database connection parameters
params = {
    "dbname": "Elden_Tracker",
    "user": "postgres",
    "password": "password",
    "host": "localhost"
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**params)
cur = conn.cursor()

# Path to your JSON file
json_file_path = 'C:/Users/kiern/Downloads/all_items.json'

# Open the JSON file and load its content
with open(json_file_path, 'r') as file:
    items = json.load(file)

# Prepare the insert query without specifying the id
insert_query = """
INSERT INTO items (name, image, description, type, effect, obtainedFrom)
VALUES %s ON CONFLICT (name) DO NOTHING;
"""


# Define a function to get item values with default if key is missing
def get_item_values(item):
    return (
        item['name'],
        item['image'],
        item['description'],
        item.get('type', 'N/A'),  # Provide a default value if 'type' is missing
        item.get('effect', 'No effect'),  # Provide a default value if 'effect' is missing
        item.get('obtainedFrom', None)  # Provide a default value if 'obtainedFrom' is missing
    )

try:
    # Use the execute_values method to efficiently insert multiple rows
    extras.execute_values(
        cur,
        insert_query,
        [get_item_values(w) for w in items],
        template=None,
        page_size=100
    )
    conn.commit()
except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    cur.close()
    conn.close()
