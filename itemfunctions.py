from extraMethods import db_connect

def search_items(item_name):
    """Search for items by name."""
    # Establish connection to the PostgreSQL database
    conn = db_connect()
    
    # Create a cursor object
    cur = conn.cursor()
    
    try:
        # Execute a query
        cur.execute("SELECT * FROM items WHERE name ILIKE %s;", (f'%{item_name}%',))
        
        # Fetch all matching records
        items = cur.fetchall()
        # Display test
        #for item in items:
        #    print(item)
        
        return items
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def add_item_to_user(user_id, item_id):
    """Add a item to the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Insert a record into the user_items table
        cur.execute("INSERT INTO user_items (user_id, item_id) VALUES (%s, %s);",
                    (user_id, item_id))
        
        # Commit the transaction
        conn.commit()
        # Display test
        #print("Item added to user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()

def delete_item_from_user(user_id, item_id):
    """Remove an item from the user's collection."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Delete the record from the user_items table
        cur.execute("DELETE FROM user_items WHERE user_id = %s AND item_id = %s;",
                    (user_id, item_id))
        
        # Commit the transaction
        conn.commit()
        # Display test
        #print("Item removed from user's collection successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()