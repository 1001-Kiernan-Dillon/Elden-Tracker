from extraMethods import db_connect

def search_talismans(talisman_name):
    """Search for talismans by name."""
    # Establish connection to the PostgreSQL database
    conn = db_connect()
    
    # Create a cursor object
    cur = conn.cursor()
    
    try:
        # Execute a query
        cur.execute("SELECT * FROM talismans WHERE name ILIKE %s;", (f'%{talisman_name}%',))
        
        # Fetch all matching records
        talismans = cur.fetchall()
        # Display Test
        #for talisman in talismans:
        #    print(talisman)
        
        return talismans
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def add_talisman_to_user(user_id, talisman_id):
    """Add a talisman to the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Insert a record into the user_weapons table
        cur.execute("INSERT INTO user_talismans (user_id, talisman_id) VALUES (%s, %s);",
                    (user_id, talisman_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Talisman added to user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()

def delete_talisman_from_user(user_id, talisman_id):
    """Remove an talisman from the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Delete the record from the user_talismans table
        cur.execute("DELETE FROM user_talismans WHERE user_id = %s AND talisman_id = %s;",
                    (user_id, talisman_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Talisman removed from user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()