import pandas as pd


def load_data():
    df = pd.read_csv("data/data.csv", encoding="cp949", thousands=",")
    return df