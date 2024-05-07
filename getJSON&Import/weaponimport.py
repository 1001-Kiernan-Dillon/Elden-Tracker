import json
import psycopg2
from psycopg2 import extras  # Make sure to import extras

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
json_file_path = 'C:/Users/kiern/Downloads/weapons.json'

# Open the JSON file and load its content
with open(json_file_path, 'r') as file:
    # Assuming the JSON structure is an array of objects
    weapons = json.load(file)

# Iterate over the weapons and insert them into the database
insert_query = """
INSERT INTO weapons (name, image, description, attack, defence, "scalesWith", "requiredAttributes", category, weight)
VALUES %s;
"""

try:
    # Use the execute_values method to efficiently insert multiple rows
    extras.execute_values(
        cur,
        insert_query,
        [(w['name'], w['image'], w['description'], json.dumps(w['attack']), json.dumps(w['defence']), json.dumps(w['scalesWith']), json.dumps(w['requiredAttributes']), w['category'], w['weight'])
         for w in weapons],
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
