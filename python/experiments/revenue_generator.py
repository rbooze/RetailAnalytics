import numpy as np

from experiments.experiment_config import EXPERIMENT
from experiments.customer_behavior import SEGMENT_MULTIPLIERS

def generate_revenue(group, segment):
    base_average = EXPERIMENT["groups"][group]["average_order_value"]

    spend_multiplier = SEGMENT_MULTIPLIERS[segment]["spend"]

    target_average = base_average * spend_multiplier

    # Why log normal? Retail sales are almost never normally distributed.
    revenue = np.random.lognormal(
        mean=np.log(target_average),
        sigma=0.45
    )

    return round(revenue, 2)