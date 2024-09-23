import pandas as pd
import re

# Load the filtered data from the previous step
input_csv = "allSeasons/23 reg/23Filtered_EVERYPEN.csv"

# Read the CSV into a dataframe
df = pd.read_csv(input_csv)


# Function to extract the penalized team acronym from the 'Description'
def extract_penalized_team(description):
    # Find matches for 'PENALTY on ___' or 'Penalty on ___', case insensitive
    match = re.search(r"penalty on (\w+)-", description, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


# Apply the extract_team function to each row in the 'Description' column
df["Penalized_Team"] = df["Description"].apply(extract_penalized_team)

# Drop rows where we couldn't extract the penalized team (just in case)
df = df.dropna(subset=["Penalized_Team"])


# Function to extract the team that benefited from the penalty
def extract_positive_team(row):
    # Assuming 'Offense' and 'Defense' fields exist in the dataframe
    if row["Penalized_Team"] == row["Offense"]:
        return row["Defense"]  # The other team benefits
    elif row["Penalized_Team"] == row["Defense"]:
        return row["Offense"]  # The other team benefits
    return None


# Apply the extract_positive_team function to each row
df["Positive_Team"] = df.apply(extract_positive_team, axis=1)

# Drop rows where we couldn't determine the benefiting team
df = df.dropna(subset=["Positive_Team"])

# Group by 'Week' and 'Positive_Team' to count the number of positive penalties for each team per week
positive_penalty_counts = (
    df.groupby(["Week", "Positive_Team"]).size().unstack(fill_value=0)
)

# Add a row for 'All Weeks' that sums the counts from all weeks
positive_penalty_counts.loc["All Weeks"] = positive_penalty_counts.sum()

# Write the result to a new CSV
positive_penalty_counts.to_csv("23_holdingPI_beneficiary.csv")

print(
    "Positive penalties by week CSV created with 'All Weeks' summary: 'Positive_Penalties_By_Week.csv'"
)
