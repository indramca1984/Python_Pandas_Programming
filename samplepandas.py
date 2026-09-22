import pandas as pd

file_path = r"C:\Users\Indra.V\Desktop\sales_data.csv"

# df = pd.read_csv(r"C:\Users\Indra.V\Desktop\sales_data.csv")

df = pd.read_csv(file_path)

print (df)

df1 = pd.read_csv(file_path, usecols=["SaleID", "Date", "Region"])


print(df1.head())

print(df.info())

print(df.columns)

print  (df[df["Quantity"] > 15])

# 1 dimensional
s = pd.Series([10, 20, 30, 40])
print(s)

# 2 dimensional
data = {
"Name": ["Indra", "John", "Alice"],
"Age": [30, 25, 28]
}
df = pd.DataFrame(data)

print (df)
print("hello")
