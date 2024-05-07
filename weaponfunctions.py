from extraMethods import db_connect

def search_weapons(weapon_name):
    """Search for weapons by name."""
    # Establish connection to the PostgreSQL database
    conn = db_connect()
    
    # Create a cursor object
    cur = conn.cursor()
    
    try:
        # Execute a query
        cur.execute("SELECT * FROM weapons WHERE name ILIKE %s;", (f'%{weapon_name}%',))
        
        # Fetch all matching records
        weapons = cur.fetchall()
        
        # Display Test
        #for weapon in weapons:
        #    print(weapon)
        
        return weapons
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def add_weapon_to_user(user_id, weapon_id):
    """Add a weapon to the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Insert a record into the user_weapons table
        cur.execute("INSERT INTO user_weapons (user_id, weapon_id) VALUES (%s, %s);",
                    (user_id, weapon_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Weapon added to user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()

def delete_weapon_from_user(user_id, weapon_id):
    """Remove an weapon from the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Delete the record from the user_weapons table
        cur.execute("DELETE FROM user_weapons WHERE user_id = %s AND weapon_id = %s;",
                    (user_id, weapon_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Weapon removed from user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()