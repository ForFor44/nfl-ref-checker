import pandas as pd
import re

# Load the filtered data from the previous step
input_csv = "allSeasons/23 reg/23Filtered_EVERYPEN.csv"

# Read the CSV into a dataframe
df = pd.read_csv(input_csv)


# Function to extract the team acronym from the 'Description'
def extract_team(description):
    # Find matches for 'PENALTY on ___' or 'Penalty on ___', case insensitive
    match = re.search(r"penalty on (\w+)-", description, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


# Apply the extract_team function to each row in the 'Description' column
df["Team"] = df["Description"].apply(extract_team)

# Drop rows where we couldn't extract the team (just in case)
df = df.dropna(subset=["Team"])

# Group by 'Week' and 'Team' to count the number of penalties for each team per week
penalty_counts = df.groupby(["Week", "Team"]).size().unstack(fill_value=0)

# Add a row for 'All Weeks' that sums the counts from all weeks
penalty_counts.loc["All Weeks"] = penalty_counts.sum()

# Write the result to a new CSV
penalty_counts.to_csv("holdingPI_23.csv")

print("Penalties by week CSV created with 'All Weeks' summary: 'Penalties_By_Week.csv'")
