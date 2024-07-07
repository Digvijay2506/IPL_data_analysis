import pandas as pd

def load_trophies_data(file_path):
    """
    Function to load trophies data from an Excel file.
    """
    df = pd.read_excel(file_path)
    return df
