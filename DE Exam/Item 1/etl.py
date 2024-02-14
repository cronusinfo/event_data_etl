import pandas as pd
import json
from sqlalchemy import create_engine

# Define the path to the events file
events_file_path = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 1\source\events.ndjson'

# Define the required fields
required_fields = [
    'event_date',
    'event_timestamp',
    'event_name',
    'ga_session_id',
    'engaged_session_event',
    'page_location',
    'page_title',
    'page_referrer',
    'source'
]

try:
    # Read the events file line by line
    data = []
    print("Reading file...")
    with open(events_file_path, 'r') as file:
        for line in file:
            # Try to parse the line as JSON
            try:
                json_data = json.loads(line)
                data.append(json_data)
            except json.JSONDecodeError:
                print(f"Skipping non-JSON line: {line.strip()}")

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Select only the required fields
    df = df[required_fields]

    # Define the connection string for MySQL
    engine = create_engine('mysql://root@localhost/data_engineer')

    # Load the DataFrame into MySQL database table
    df.to_sql('events', con=engine, if_exists='append', index=False)

    print("Data successfully loaded into the database.")

    # Read data from events_table into a DataFrame
    query = "SELECT * FROM events"
    df_events = pd.read_sql_query(query, engine)

    # Define the path to the target folder
    target_folder = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 1\target'

    # Define the path to the output CSV file
    output_csv_file = target_folder + r'\events.csv'

    # Save DataFrame to CSV
    df_events.to_csv(output_csv_file, index=False)

    print("Data successfully saved as events.csv in the target folder.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
