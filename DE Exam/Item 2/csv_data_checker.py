import pandas as pd
import os

def load_data(directory):
    try:
        # Load date.csv into a DataFrame
        date_df = pd.read_csv(os.path.join(directory, 'date.csv'))
        expected_date_headers = ['DATE_KEY', 'DATE_FLD', 'DATE_NAME', 'DATE_KEY_LY', ...]  # Add all expected headers
        if not all(header in date_df.columns for header in expected_date_headers):
            print("Error: Incorrect headers in date.csv")
            return None, None, None
        date_df['DATE_FLD'] = pd.to_datetime(date_df['DATE_FLD'])
        date_df['DATE_FLD_LY'] = pd.to_datetime(date_df['DATE_FLD_LY'])

        # Load stores.csv into a DataFrame
        stores_df = pd.read_csv(os.path.join(directory, 'stores.csv'))
        expected_stores_headers = ['STORE_KEY', 'STORE_CODE', 'STORE_DESCRIPTION']  # Add all expected headers
        if not all(header in stores_df.columns for header in expected_stores_headers):
            print("Error: Incorrect headers in stores.csv")
            return None, None, None

        # Load fsl.csv into a DataFrame
        fsl_df = pd.read_csv(os.path.join(directory, 'fsl.csv'))
        expected_fsl_headers = ['DATE_KEY', 'STORE_KEY', 'SALE_NET_VAL']  # Add all expected headers
        if not all(header in fsl_df.columns for header in expected_fsl_headers):
            print("Error: Incorrect headers in fsl.csv")
            return None, None, None

        return date_df, stores_df, fsl_df
    except FileNotFoundError:
        print("CSV files not found. Please ensure they exist in the specified directory.")
        return None, None, None

def main():
    # Specify the directory containing the CSV files
    directory = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 2'

    # Load data
    date_df, stores_df, fsl_df = load_data(directory)

    if date_df is None or stores_df is None or fsl_df is None:
        return

    # Add your data processing logic here

if __name__ == "__main__":
    main()
