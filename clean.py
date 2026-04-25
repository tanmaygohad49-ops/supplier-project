import pandas as pd
import json

with open("../data_raw.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

df["price"] = df["price"].astype(str)

df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["price"] = df["price"].fillna(0)

df["in_stock"] = df["availability"].apply(
    lambda x: 1 if "In stock" in str(x) else 0
)

df = df.drop(columns=["availability"])

df.to_csv("../clean_data.csv", index=False)

print("Cleaning done ✔ Rows:", len(df))