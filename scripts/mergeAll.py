import pandas as pd

# List of CSV file names
csv_files = [
    "allSeasons/22 reg/4thdownALLPEN.csv",
    "allSeasons/22 reg/PENonSCORINGDRIVES.csv",
    "allSeasons/22 reg/22Filtered_EVERYPEN.csv",
    "allSeasons/22 reg/4thdownALLPEN.csv",
]

# Empty list to store dataframes
dfs = []

# Loop through each CSV file
for csv_file in csv_files:
    # Read the CSV file into a dataframe
    df = pd.read_csv(csv_file)

    # Append dataframe to the list
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Drop duplicates based on the 'Description' column
unique_df = combined_df.drop_duplicates(subset=["Description"])

# Write the resulting dataframe to a new CSV file
unique_df.to_csv("Unique_Combined.csv", index=False)

print("Combined CSV with unique 'Description' entries created: 'Unique_Combined.csv'")
