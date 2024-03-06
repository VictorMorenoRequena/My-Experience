import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Define the start and end dates
start_date = '2023-01-01'
end_date = '2025-01-01'  # 3 years from the start date

# Generate the date range
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Create the DataFrame
data = pd.DataFrame({'Date': dates})

# Format the dates to "MM/DD/YYYY" format
data['Date'] = data['Date'].dt.strftime('%m/%d/%Y')

# Add a new column "Caja" initialized with 0
data['Caja'] = 0

# Display the first few rows to check
print(data)


data.to_excel('cajas.xlsx', index=False)

