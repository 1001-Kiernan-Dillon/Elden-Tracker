import json
import psycopg2

# Database connection parameters
params = {
    "dbname": "Elden_Tracker",
    "user": "postgres",
    "password": "password",
    "host": "localhost"
}

# JSON file path
json_file_path = 'C:/Users/kiern/Downloads/all_bosses.json'

# Connect to the PostgreSQL database
conn = psycopg2.connect(**params)
cur = conn.cursor()

# Open the JSON file
with open(json_file_path, mode='r') as file:
    # Load the data
    bosses_data = json.load(file)

    # Iterate over the data
    for boss in bosses_data:
        # Prepare the INSERT statement
        insert_query = """
        INSERT INTO "bossTest" (name, image, region, description, location, drops, "healthPoints")
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        # Convert drops list to a PostgreSQL array format
        drops_array = boss['drops'] if boss['drops'] is not None else []

        # Execute the INSERT statement
        cur.execute(insert_query, (
            boss['name'],
            boss['image'],
            boss['region'],
            boss['description'],
            boss['location'],
            drops_array,
            boss['healthPoints'] if boss['healthPoints'] is not None else None
        ))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Bosses data has been imported successfully.")
