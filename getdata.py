# importing the dataset from the google sheets document.

sheet_url = "https://docs.google.com/spreadsheets/d/1CRS-mgp2RASq4pzmz9rpcXhszWjBMmaX2Ntdk2_RZCc/edit?usp=sharing"
sheet_id = sheet_url.split('/d/')[1].split('/edit')[0]
sheet_name = "Dataset"  # Replace with your actual sheet name

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)
# print(df.head())

#Fill Nan
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df.fillna({col: df[col].mean()}, inplace=True)
    else:
        df.fillna({col: df[col].mode()[0]}, inplace=True)
