import pandas as pd

def load_ratings(path):
    ratings = pd.read_csv(path)
    return ratings
    