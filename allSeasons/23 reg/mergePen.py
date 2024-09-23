import pandas as pd

# List of CSV file names
csv_files = [
    'EVERYPEN(1-4).csv',
    'EVERYPEN(5-8).csv',
    'EVERYPEN(9-12).csv',
    'EVERYPEN(13-18).csv'
]

# Empty list to store filtered dataframes
filtered_dfs = []

# Loop through each CSV file
for csv_file in csv_files:
    # Read the CSV file into a dataframe
    df = pd.read_csv(csv_file)
    
    # Filter rows where 'Description' contains 'Holding' or 'Pass Interference'
    filtered_df = df[df['Description'].str.contains('Holding|Pass Interference', case=False, na=False)]
    
    # Append filtered dataframe to the list
    filtered_dfs.append(filtered_df)

# Concatenate all filtered dataframes
combined_df = pd.concat(filtered_dfs, ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('Filtered_EVERYPEN.csv', index=False)

print("Filtered CSV created: 'Filtered_EVERYPEN.csv'")
