import pandas as pd
import datetime
import os

def load_data(directory):
    try:
        # Load date.csv into a DataFrame
        date_df = pd.read_csv(os.path.join(directory, 'date.csv'))
        date_df['DATE_FLD'] = pd.to_datetime(date_df['DATE_FLD'])
        date_df['DATE_FLD_LY'] = pd.to_datetime(date_df['DATE_FLD_LY'])

        # Load stores.csv into a DataFrame
        stores_df = pd.read_csv(os.path.join(directory, 'stores.csv'))

        # Load fsl.csv into a DataFrame
        fsl_df = pd.read_csv(os.path.join(directory, 'fsl.csv'))

        return date_df, stores_df, fsl_df
    except FileNotFoundError:
        print("CSV files not found. Please ensure they exist in the specified directory.")
        return None, None, None

def main():
    # Specify the directory where the CSV files are located
    directory = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 2'

    # Load data
    date_df, stores_df, fsl_df = load_data(directory)

    if date_df is None or stores_df is None or fsl_df is None:
        return

    # Merge date_df with fsl_df on DATE_KEY
    merged_df = pd.merge(fsl_df, date_df, on='DATE_KEY')

    # Get today's date
    today = datetime.datetime.today()

    # Filter data for YTD sales
    ytd_sales = merged_df[(merged_df['DATE_FLD'] >= pd.Timestamp(today.year, 1, 1)) & 
                          (merged_df['DATE_FLD'] <= today)]
    ytd_total_sales = ytd_sales['SALE_NET_VAL'].sum()

    # Filter data for MTD sales
    mtd_sales = merged_df[(merged_df['DATE_FLD'] >= pd.Timestamp(today.year, today.month, 1)) & 
                          (merged_df['DATE_FLD'] <= today)]
    mtd_total_sales = mtd_sales['SALE_NET_VAL'].sum()

    # Filter data for WTD sales
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)
    wtd_sales = merged_df[(merged_df['DATE_FLD'] >= start_of_week) & 
                          (merged_df['DATE_FLD'] <= end_of_week)]
    wtd_total_sales = wtd_sales['SALE_NET_VAL'].sum()

    # Print results
    print("\nYear-To-Date Sales:", ytd_total_sales)
    print("Month-To-Date Sales:", mtd_total_sales)
    print("Week-To-Date Sales:", wtd_total_sales)

    # Print the filtered dataframes
    print("\nFiltered Data for Year-To-Date Sales:")
    print(ytd_sales.head())

    print("\nFiltered Data for Month-To-Date Sales:")
    print(mtd_sales.head())

    print("\nFiltered Data for Week-To-Date Sales:")
    print(wtd_sales.head())

if __name__ == "__main__":
    main()
