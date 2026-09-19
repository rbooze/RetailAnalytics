"""
Experiment configuration.

This file contains all business assumptions.
Changing these values changes the experiment
without changing the simulation code.
"""

EXPERIMENT = {
    "experiment_id": 1,
    "analysis_start": "2026-01-01",
    "analysis_end": "2026-03-31",

    "groups": {
        "Control": {
            "purchase_probability": 0.18,
            "average_order_value": 275,
            "profit_margin": 0.45,
            "return_probability": 0.06
        },

        "Treatment": {
            "purchase_probability": 0.24,
            "average_order_value": 310,
            "profit_margin": 0.43,
            "return_probability": 0.08
        }
    }
}