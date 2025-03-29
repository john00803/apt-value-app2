# auth/user_loader.py

import pandas as pd


def load_users_from_csv(csv_path="users.csv"):
    try:
        return pd.read_csv(csv_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["email"])


def is_valid_user(email, csv_path="users.csv"):
    df = load_users_from_csv(csv_path)
    return email in df["email"].values
