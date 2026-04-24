import pandas as pd
df = pd.DataFrame({
    "name": ["Amy", "Bob", "Cathy", "David", "Evan", "Fiona"],
    "age": [20, 21, 19, 22, 20, 23],
    "score": [88, 92, 79, 85, 90, 95]
})
df["passed"] = df["score"] >= 90
print(df)
df["score"] = df["score"] + 5