import numpy as np
import csv

product_names = []
stock_qty = []
unit_price = []
sales_volume = []

with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product_names.append(row["Product_Name"])
        stock_qty.append(float(row["Stock_Quantity"].strip()))

        price = row["Unit_Price"].replace("$", "").replace(",", "").strip()
        unit_price.append(float(price))
        sales_volume.append(float(row["Sales_Volume"].strip()))

# 轉 NumPy
product_names = np.array(product_names)
stock_qty = np.array(stock_qty)
unit_price = np.array(unit_price)
sales_volume = np.array(sales_volume)

# 檢查資料是否為空
print("資料筆數:", len(product_names))

# 庫存價值
inventory_value = stock_qty * unit_price
print(inventory_value)

# 最暢銷
print("最暢銷:", product_names[np.argmax(sales_volume)])

# 打9折收入
discount_revenue = sales_volume * unit_price * 0.9
print(discount_revenue)
# 輸出
with open("StudentID_name_Numpy_1.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 寫入標題列
    writer.writerow(["Product_Name", "Inventory_Value", "Discount_Revenue"])
    # 寫入每一筆資料
    for name, inv, rev in zip(product_names, inventory_value, discount_revenue):
        writer.writerow([name, round(inv, 2), round(rev, 2)])

print("檔案已輸出：StudentID_name_Numpy.csv")