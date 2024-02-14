import pandas as pd

# Define the directory path
directory = r'C:\Users\63976\Downloads\DE Exam\DE Exam\Item 2'

# Read the date dataset
date_df = pd.read_csv(directory + r'\date.csv')

# Read the stores dataset
stores_df = pd.read_csv(directory + r'\stores.csv')

# Read the sales dataset
fsl_df = pd.read_csv(directory + r'\fsl.csv')

# Convert DATE_KEY column to integer
fsl_df['DATE_KEY'] = fsl_df['DATE_KEY'].astype(int)

# Verify that there are sales data entries in the sales dataset for the current year, month, and week
current_year = pd.Timestamp.now().year
current_month = pd.Timestamp.now().month
current_week = pd.Timestamp.now().week

current_year_sales = fsl_df[fsl_df['DATE_KEY'] // 10000 == current_year]
current_month_sales = fsl_df[(fsl_df['DATE_KEY'] // 100) % 100 == current_month]
current_week_sales = fsl_df[((fsl_df['DATE_KEY'] // 100) % 100 == current_month) 
                            & (fsl_df['DATE_KEY'] % 100 == current_week)]

# Display the counts of sales data entries for the current year, month, and week
print("Sales entries for the current year:", len(current_year_sales))
print("Sales entries for the current month:", len(current_month_sales))
print("Sales entries for the current week:", len(current_week_sales))

# Display the first few rows of each dataset to verify the data has been read correctly
print("\nDate dataset:")
print(date_df.head())

print("\nStores dataset:")
print(stores_df.head())

print("\nSales dataset:")
print(fsl_df.head())
