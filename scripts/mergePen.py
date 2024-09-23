import pandas as pd

# Load in your season's PEN csv's here
csv_files = [
    "allSeasons/22 playoffs/EVERYPENdivisional.csv",
]

for file in csv_files:
    try:
        df = pd.read_csv(file)
        print(f"Successfully loaded {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")
    except PermissionError:
        print(f"Permission denied: {file}")
    except pd.errors.ParserError:
        print(f"Error parsing CSV: {file}")
# Empty list to store filtered dataframes
filtered_dfs = []

# Loop through each CSV file
for csv_file in csv_files:
    # Read the CSV file into a dataframe
    df = pd.read_csv(csv_file)

    # Filter rows where 'Description' contains 'Holding' or 'Pass Interference'
    filtered_df = df[
        df["Description"].str.contains(
            "Holding|Pass Interference", case=False, na=False
        )
    ]

    # Append filtered dataframe to the list
    filtered_dfs.append(filtered_df)

# Concatenate all filtered dataframes
combined_df = pd.concat(filtered_dfs, ignore_index=True)

# Set this to your corresponding season filtered everypen
combined_df.to_csv("divPlayoffs_22Filtered_EVERYPEN.csv", index=False)

print("Filtered CSV created: 'Filtered_EVERYPEN.csv'")
