import pandas as pd
df = pd.read_csv("score_Pandas_2.csv")
# 檢視資料筆數與前幾筆
print("資料筆數：", df.shape)
print(df.head())

# 篩選（class = A 且 score >= 80）
df_filter = df[(df["class"] == "A") & (df["score"] >= 80)]
print("\n篩選後資料：")
print(df_filter)

# 以 class 分組（對應 Product line）
group_class = df.groupby("class").agg({
    "score": "mean"
}).reset_index()

print("\n各班平均分數：")
print(group_class)

# 依 class 分組（統計人數）
group_count = df.groupby("class").agg({
    "score": "count"
}).rename(columns={"score": "Student Count"}).reset_index()

print("\n各班人數：")
print(group_count)

# 找出最高分學生
top_student = df.loc[df["score"].idxmax()]
print("\n最高分學生：")
print(top_student)

# 輸出 CSV
group_class.to_csv("StudentID_name_pandas_W13.csv", index=False)