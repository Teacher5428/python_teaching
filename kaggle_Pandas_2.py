import pandas as pd
df = pd.read_csv("SuperMarket Analysis.csv")

#  檢視資料筆數與前幾筆
print("資料筆數：", df.shape)
print(df.head())

#  篩選 Branch = A 且 Customer type = Member
df_filter = df[(df["Branch"] == "A") & (df["Customer type"] == "Member")]
print("\n篩選後資料：")
print(df_filter.head())

#  以 Product line 分組
group_product = df.groupby("Product line").agg({
    "Sales": "sum",
    "Rating": "mean"
}).reset_index()

print("\n各產品線銷售與評分：")
print(group_product)

# 依 City 與 Gender 分組
group_city_gender = df.groupby(["City", "Gender"]).agg({
    "Sales": "mean",
    "Invoice ID": "count"
}).rename(columns={"Invoice ID": "Transaction Count"}).reset_index()

print("\nCity + Gender 統計：")
print(group_city_gender)

#  找出銷售最高產品線
top_product = group_product.loc[group_product["Sales"].idxmax()]
print("\n銷售最高產品線：")
print(top_product)

# 輸出 CSV（請改成你的學號與名字）
group_product.to_csv("StudentID_name_pandas_2.csv", index=False)