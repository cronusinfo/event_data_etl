from sqlalchemy import create_engine

# Define the connection string for MySQL
connection_string = 'mysql://root@localhost/data_engineer'

# Try to create the engine
try:
    engine = create_engine(connection_string)
    # Try to connect to the database
    with engine.connect() as connection:
        print("Connection to MySQL database successful.")
except Exception as e:
    print("Error connecting to MySQL database:", e)
