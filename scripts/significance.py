import pandas as pd
import scipy.stats as stats

# Load penalty data
penalty_data_csv = "insights/regular_23.csv"  # Updated with actual file path
beneficiary_data_csv = (
    "insights/23_beneficiary_regular.csv"  # Updated with actual file path
)

# Read the CSVs into dataframes
penalties_df = pd.read_csv(penalty_data_csv, index_col="Week")
beneficiaries_df = pd.read_csv(beneficiary_data_csv, index_col="Week")

# Remove the 'All Weeks' summary row for statistical analysis
penalties_df = penalties_df.drop("All Weeks", errors="ignore")
beneficiaries_df = beneficiaries_df.drop("All Weeks", errors="ignore")

# Summing penalties and beneficiaries for each team across all weeks
penalties_total = penalties_df.sum()
beneficiaries_total = beneficiaries_df.sum()

# Perform Chi-Square test for penalties
chi2_penalties, p_penalties = stats.chisquare(penalties_total)
print(
    f"Chi-Square Test for Penalties: Chi2 = {chi2_penalties}, p-value = {p_penalties}"
)

# Perform Chi-Square test for beneficiaries
chi2_beneficiaries, p_beneficiaries = stats.chisquare(beneficiaries_total)
print(
    f"Chi-Square Test for Beneficiaries: Chi2 = {chi2_beneficiaries}, p-value = {p_beneficiaries}"
)

# Interpretation
alpha = 0.05  # Significance level

if p_penalties < alpha:
    print(
        "The distribution of penalties across teams is statistically significant (not uniform)."
    )
else:
    print(
        "The distribution of penalties across teams is not statistically significant (uniform)."
    )

if p_beneficiaries < alpha:
    print(
        "The distribution of beneficiaries across teams is statistically significant (not uniform)."
    )
else:
    print(
        "The distribution of beneficiaries across teams is not statistically significant (uniform)."
    )
