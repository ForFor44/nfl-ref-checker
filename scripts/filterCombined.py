import pandas as pd

# The CSV file we created earlier
input_csv = "allSeasons/22 playoffs/divPlayoffs_22Unique_Combined.csv"

# Array of strings to filter out
filter_out_strings = [
    "False Start",
    "Delay of Game",
    "Neutral Zone Infraction",
    "Running Into the Kicker",
    "Roughing the Kicker",
    "Too Many Men on Field",
]

# Read the Unique_Combined CSV into a dataframe
df = pd.read_csv(input_csv)

# Use a boolean mask to filter out rows containing any of the unwanted strings
# We'll use a combination of str.contains and negate the match using ~
filter_pattern = "|".join(filter_out_strings)  # Create a regex pattern from the list
filtered_df = df[~df["Description"].str.contains(filter_pattern, case=False, na=False)]

# Write the filtered dataframe to a new CSV file
filtered_df.to_csv("divPlayoffs_22Filtered_Unique_Combined.csv", index=False)

print("Filtered CSV created: 'Filtered_Unique_Combined.csv'")
