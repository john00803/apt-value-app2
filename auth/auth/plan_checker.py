# auth/plan_checker.py

import pandas as pd


def load_plan_names(csv_path="plan_names.csv"):
    try:
        return pd.read_csv(csv_path)["name"].tolist()
    except FileNotFoundError:
        return []


def is_valid_plan_name(name, csv_path="plan_names.csv"):
    plan_names = load_plan_names(csv_path)
    return name in plan_names
