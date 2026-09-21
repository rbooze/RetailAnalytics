"""
A/B Test Effect Size Analysis

Measures:
- Absolute lift
- Relative lift
- Confidence interval
- Incremental customers
- Incremental profit
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

control_profit = float(control["Profit"])
treatment_profit = float(treatment["Profit"])

# -------------------------------
# Conversion Rates
# -------------------------------
control_rate = (control_purchases / control_customers)

treatment_rate = (treatment_purchases / treatment_customers)

# -------------------------------
# Lift Calculations
# -------------------------------
absolute_lift = (treatment_rate - control_rate)

relative_lift = (absolute_lift / control_rate) * 100

# -------------------------------
# Confidence Interval
# -------------------------------
standard_error = math.sqrt(
    (treatment_rate * (1 - treatment_rate) / treatment_customers) + (control_rate * (1 - control_rate) / control_customers)
)

margin_error = 1.96 * standard_error

lower_bound = absolute_lift - margin_error

upper_bound = absolute_lift + margin_error

# -------------------------------
# Incremental Customers
# -------------------------------
expected_control_purchases = (control_rate * treatment_customers)

incremental_customers = (treatment_purchases - expected_control_purchases)

# -------------------------------
# Incremental Profit
# -------------------------------
incremental_profit = (treatment_profit - control_profit)

# -------------------------------
# Results
# -------------------------------
print("\nConversion Rates")

print("Control:", round(control_rate * 100, 2), "%")    # Baseline performance

print("Treatment:", round(treatment_rate * 100, 2), "%")    # Promotion improved conversions

print("\nEffect Size")

print("Absolute Lift:", round(absolute_lift * 100, 2), "percentage points")

print("Relative Lift:", round(relative_lift, 2), "%")   # Improvement over the baseline conversion rate

print("\n95% Confidence Interval")      # How big is that difference likely to be?

print(round(lower_bound * 100, 2), "% to", round(upper_bound * 100, 2), "%")

print("\nBusiness Impact")

print("Incremental Customers:", round(incremental_customers))   # Additional customers who purchased because of the promotion

print("Incremental Profit: $", round(incremental_profit, 2))    # Financial impact despite lower margins