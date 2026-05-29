import pandas as pd

def get_test_data():
    file = "fixtures/data.xlsx"
    df = pd.read_excel(file)

    return df.iloc[0].to_dict()