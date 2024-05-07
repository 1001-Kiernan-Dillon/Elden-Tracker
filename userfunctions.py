import psycopg2
from psycopg2 import sql
from extraMethods import db_connect

def get_user_id(username):
    """Retrieve a user's ID from the users table."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Query the users table
        cur.execute("SELECT user_id FROM users WHERE username = %s;", (username,))
        
        # Fetch the user ID
        user_id = cur.fetchone()
        
        if user_id is not None:
            return user_id[0]
        else:
            return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()

def get_password(username):
    """Retrieve a user's password from the users table."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Query the users table
        cur.execute("SELECT password FROM users WHERE username = %s;", (username,))
        
        # Fetch the password
        password = cur.fetchone()
        
        if password is not None:
            return password[0]
        else:
            return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()


def create_user(username, email, password):
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = db_connect()
        cur = conn.cursor()

        # Insert new user into the users table
        cur.execute(
            sql.SQL("INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING user_id;"),
            (username, email, password)
        )
        
        # Get the generated id
        user_id = cur.fetchone()[0]
        conn.commit()
        
        print(f"User created successfully with user_id: {user_id}")
        
        # Close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Example usage
#create_user('new_user', 'new_user@example.com', 'secure_password')

def delete_user(user_id):
    """Delete a user from the users table."""
    conn = db_connect()
    cur = conn.cursor()
    
    try:
        # Delete the user from the users table
        cur.execute("DELETE FROM users WHERE user_id = %s;", (user_id,))
        
        # Commit the transaction
        conn.commit()
        print("User deleted successfully.")
    
    except Exception as e:
        # If there is any error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")
    
    finally:
        cur.close()
        conn.close()
