import pandas as pd

# Define the expected headers for date.csv
expected_headers = ['DATE_KEY', 'DATE_FLD', 'DATE_NAME', 'DATE_KEY_LY', 'DATE_FLD_LY']

# Load date.csv and check its headers
date_csv_path = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 2\date.csv'
date_df = pd.read_csv(date_csv_path)
actual_headers = date_df.columns.tolist()

# Check if the actual headers match the expected headers
if actual_headers != expected_headers:
    print(f"Error: Incorrect headers in {date_csv_path}")
    print(f"Expected headers: {expected_headers}")
    print(f"Actual headers: {actual_headers}")

    # Correct the headers
    date_df = date_df[expected_headers]

    # Save the corrected DataFrame back to date.csv
    date_df.to_csv(date_csv_path, index=False)

    print("Headers have been corrected and saved.")
else:
    print(f"Headers in {date_csv_path} are correct.")
