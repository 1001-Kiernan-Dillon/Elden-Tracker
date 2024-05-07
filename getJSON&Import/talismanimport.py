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

# Path to your JSON file with talisman data
json_file_path = 'C:/Users/kiern/Downloads/all_talismans.json'

# Open the JSON file and load its content
with open(json_file_path, 'r') as file:
    talismans = json.load(file)

# Prepare the insert query
insert_query = """
INSERT INTO talismans (name, image, description, effects)
VALUES %s;
"""

# Define a function to get talisman values
def get_talisman_values(talisman):
    return (
        talisman['name'],
        talisman['image'],
        talisman['description'],
        talisman.get('effects', 'No effects')  # Provide a default value if 'effects' is missing
    )

try:
    # Use the execute_values method to efficiently insert multiple rows
    extras.execute_values(
        cur,
        insert_query,
        [get_talisman_values(t) for t in talismans],
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
