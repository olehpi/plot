import pandas as pd


def read_csv(file_path, decimal=','):
    with open(file_path, newline='', mode='r') as file:
        df = pd.read_csv(file_path, sep=";", decimal=decimal)
    return df
