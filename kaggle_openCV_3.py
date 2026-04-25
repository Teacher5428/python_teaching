import cv2
import os
data_dir = "data"
output_dir = "output"
# 建立輸出資料夾
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# -----------------------------
# 載入 Haar 人臉模型
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# 統計用變數
# -----------------------------
count = {"Sad": 0, "Angry": 0, "Happy": 0}

# -----------------------------
# 讀取三個資料夾
# -----------------------------
for label in ["Sad", "Angry", "Happy"]:
    folder_path = os.path.join(data_dir, label)

    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)

        img = cv2.imread(img_path)

        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # -----------------------------
        # 人臉偵測
        # -----------------------------
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # -----------------------------
        # 標註表情文字
        # -----------------------------
        cv2.putText(
            img,
            label,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        # -----------------------------
        # 統計數量
        # -----------------------------
        count[label] += 1

        # -----------------------------
        # 儲存結果
        # -----------------------------
        save_path = os.path.join(output_dir, f"{label}_{filename}")
        cv2.imwrite(save_path, img)

# -----------------------------
# 輸出統計結果
# -----------------------------
print("=== 表情統計結果 ===")
for k, v in count.items():
    print(f"{k}: {v} 張")

print("處理完成，結果已輸出到 output 資料夾")