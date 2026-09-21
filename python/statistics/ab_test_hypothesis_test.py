"""
A/B Test Hypothesis Testing

Question:
Did the win-back promotion increase purchase rate?

Test:
Two-Proportion Z-Test
"""

import math
import sys
from pathlib import Path
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# -------------------------------
# Experiment Results
# -------------------------------
from common.database import read_sql

query = """

SELECT
    GroupName,
    Customers,
    Purchasers,
    Revenue,
    Profit
FROM Analytics.vw_ExperimentSummary WITH (NOLOCK)
WHERE 
    ExperimentID = 1

"""

results = read_sql(query)

control = results[results["GroupName"] == "Control"].iloc[0]

treatment = results[results["GroupName"] == "Treatment"].iloc[0]

control_customers = int(control["Customers"])
control_purchases = int(control["Purchasers"])

treatment_customers = int(treatment["Customers"])
treatment_purchases = int(treatment["Purchasers"])

# -------------------------------
# Calculate Conversion Rates
# -------------------------------
control_rate = (control_purchases / control_customers)

treatment_rate = (treatment_purchases / treatment_customers)

print("Control Purchase Rate:", round(control_rate,4))

print("Treatment Purchase Rate:", round(treatment_rate,4))

# -------------------------------
# Hypotheses
# -------------------------------
print()

print("Null Hypothesis (H0):")
print("Treatment does not change purchase rate")

print()

print("Alternative Hypothesis (H1):")
print("Treatment increases purchase rate")

# -------------------------------
# Two-Proportion Z-Test
# -------------------------------
pooled_rate = ((control_purchases + treatment_purchases) / (control_customers + treatment_customers))

standard_error = math.sqrt(pooled_rate * (1 - pooled_rate) * ((1 / control_customers) + (1 / treatment_customers)))

z_score = (treatment_rate - control_rate) / standard_error

p_value = (1 - norm.cdf(z_score))

print()

print("Z Score:", round(z_score,4))

print("P Value:", round(p_value,6))

# -------------------------------
# Decision
# -------------------------------
alpha = 0.05

print()

if p_value < alpha:
    print("Result: Reject H0")
    print("The promotion significantly increased purchases.")
else:
    print("Result: Fail to reject H0")
    print("No significant improvement detected.")