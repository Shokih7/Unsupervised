import pandas as pd

class GetData:

    def __init__(self):
        self.sheet_url = "https://docs.google.com/spreadsheets/d/1CRS-mgp2RASq4pzmz9rpcXhszWjBMmaX2Ntdk2_RZCc/edit?usp=sharing"
        self.sheet_id = self.sheet_url.split('/d/')[1].split('/edit')[0]
        self.sheet_name = "Dataset"  # Replace with your actual sheet name
        self.url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet_name}"
        self.df = self.create_new_df()

    def create_new_df(self):
        df = pd.read_csv(self.url)
        #Fill Nan
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df.fillna({col: df[col].mean()}, inplace=True)
            else:
                df.fillna({col: df[col].mode()[0]}, inplace=True)
        return df