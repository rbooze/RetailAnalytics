"""
Profit Generator

Calculates realistic profit after:
- Product cost
- Fulfillment costs
- Promotion costs
"""

import numpy as np
from experiments.experiment_config import EXPERIMENT

def generate_profit(
    revenue,
    group
):

    if revenue == 0:
        return 0.00

    # Product cost (COGS)
    product_cost = revenue * np.random.uniform(
        0.35,
        0.55
    )

    # Warehouse + shipping
    fulfillment_cost = revenue * np.random.uniform(
        0.05,
        0.12
    )

    # Marketing cost
    # Treatment customers received a promotion
    if group == "Treatment":
        marketing_cost = revenue * 0.10
    else:
        marketing_cost = 0

    profit = (
        revenue - product_cost - fulfillment_cost - marketing_cost
    )

    return round(
        max(profit, 0),
        2
    )