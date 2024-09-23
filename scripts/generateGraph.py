import pandas as pd
import matplotlib.pyplot as plt

# Load penalty data
penalty_data_csv = "insights/holdingPI_21.csv"  # Updated with actual file path
beneficiary_data_csv = (
    "insights/21_holdingPI_beneficiary.csv"  # Updated with actual file path
)

# Dictionary of NFL teams and their corresponding colors (example colors)
team_colors = {
    "ARI": "#97233F",  # Arizona Cardinals
    "ATL": "#A71930",  # Atlanta Falcons
    "BAL": "#241773",  # Baltimore Ravens
    "BUF": "#00338D",  # Buffalo Bills
    "CAR": "#0085CA",  # Carolina Panthers
    "CHI": "#C83803",  # Chicago Bears
    "CIN": "#FB4F14",  # Cincinnati Bengals
    "CLE": "#311D00",  # Cleveland Browns
    "DAL": "#041E42",  # Dallas Cowboys
    "DEN": "#FB4F14",  # Denver Broncos
    "DET": "#0076B6",  # Detroit Lions
    "GB": "#203731",  # Green Bay Packers
    "HOU": "#03202F",  # Houston Texans
    "IND": "#002C5F",  # Indianapolis Colts
    "JAX": "#006778",  # Jacksonville Jaguars
    "KC": "#E31837",  # Kansas City Chiefs
    "LA": "#003594",  # Los Angeles Rams
    "LAC": "#0073CF",  # Los Angeles Chargers
    "LV": "#A5ACAF",  # Las Vegas Raiders
    "MIA": "#008E97",  # Miami Dolphins
    "MIN": "#4F2683",  # Minnesota Vikings
    "NE": "#002244",  # New England Patriots
    "NO": "#D3BC8D",  # New Orleans Saints
    "NYG": "#0B2265",  # New York Giants
    "NYJ": "#125740",  # New York Jets
    "PHI": "#004C54",  # Philadelphia Eagles
    "PIT": "#FFB612",  # Pittsburgh Steelers
    "SEA": "#002244",  # Seattle Seahawks
    "SF": "#AA0000",  # San Francisco 49ers
    "TB": "#D50A0A",  # Tampa Bay Buccaneers
    "TEN": "#4B92DB",  # Tennessee Titans
    "WAS": "#773141",  # Washington Commanders
}

# Read the CSVs into dataframes
penalties_df = pd.read_csv(penalty_data_csv, index_col="Week")
beneficiaries_df = pd.read_csv(beneficiary_data_csv, index_col="Week")

# Remove the 'All Weeks' summary row for cumulative analysis
penalties_df = penalties_df.drop("All Weeks", errors="ignore")
beneficiaries_df = beneficiaries_df.drop("All Weeks", errors="ignore")

# Convert the index (Week) to numeric for plotting
penalties_df.index = pd.to_numeric(penalties_df.index)
beneficiaries_df.index = pd.to_numeric(beneficiaries_df.index)

# Calculate cumulative sums by team
penalties_cumulative = penalties_df.cumsum()
beneficiaries_cumulative = beneficiaries_df.cumsum()

# Plot cumulative penalties for each team with team-specific colors
plt.figure(figsize=(10, 8))
for team in penalties_cumulative.columns:
    color = team_colors.get(team, "#000000")  # Default to black if team not found
    plt.plot(
        penalties_cumulative.index.values,
        penalties_cumulative[team].values,
        label=team,
        color=color,
    )

plt.title("21HPI_Cumulative Penalties by Team")
plt.xlabel("Week")
plt.ylabel("Number of Penalties")
plt.legend(title="Team", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Save the penalties graph
plt.savefig("21HPI_Cumulative_Penalties_Team_Colors.png")
plt.show()

# Plot cumulative beneficiaries for each team with team-specific colors
plt.figure(figsize=(10, 8))
for team in beneficiaries_cumulative.columns:
    color = team_colors.get(team, "#000000")  # Default to black if team not found
    plt.plot(
        beneficiaries_cumulative.index.values,
        beneficiaries_cumulative[team].values,
        label=team,
        color=color,
    )

plt.title("21HPI_Cumulative Beneficiaries of Penalties by Team")
plt.xlabel("Week")
plt.ylabel("Number of Beneficiaries")
plt.legend(title="Team", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Save the beneficiaries graph
plt.savefig("21HPI_Cumulative_Beneficiaries_Team_Colors.png")
plt.show()
