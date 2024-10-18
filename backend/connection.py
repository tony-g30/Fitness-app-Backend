import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'fitness',
    'user': 'abdirahman',
    'password': '37571598a',
    'host': 'localhost',  #
    'port': '5432'       
}

try:
    # Establish a connection
    conn = psycopg2.connect(**db_params)
    print("Connection successful")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Database version:", db_version)

except Exception as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()