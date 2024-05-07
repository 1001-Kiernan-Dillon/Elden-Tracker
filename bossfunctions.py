from extraMethods import db_connect

def search_bosses(boss_name):
    """Search for bosses by name."""
    # Establish connection to the PostgreSQL database
    conn = db_connect()
    
    # Create a cursor object
    cur = conn.cursor()
    
    try:
        # Execute a query
        cur.execute("SELECT * FROM bosses WHERE name ILIKE %s;", (f'%{boss_name}%',))
        
        # Fetch all matching records
        bosses = cur.fetchall()
        # Display Test
        #for boss in bosses:
        #    print(boss)
        
        return bosses
    
    except Exception as e:
        print(f"An error occurred in boss: {e}")
        return []
    
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def add_boss_to_user(user_id, boss_id):
    """Add a boss to the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Insert a record into the user_bosses table
        cur.execute("INSERT INTO user_bosses (user_id, boss_id) VALUES (%s, %s);",
                    (user_id, boss_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Boss added to user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()

def delete_boss_from_user(user_id, boss_id):
    """Remove an boss from the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Delete the record from the user_bosses table
        cur.execute("DELETE FROM user_bosses WHERE user_id = %s AND boss_id = %s;",
                    (user_id, boss_id))
        
        # Commit the transaction
        conn.commit()
        # Display Test
        #print("Boss removed from user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()