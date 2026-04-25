import cv2
import os

folder_path = "face"
output_dir = "face_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# -----------------------------
# 載入 Haar 人臉模型
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# 統計
# -----------------------------
count = 0

# -----------------------------
# 讀取資料夾所有圖片
# -----------------------------
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
    # 標註文字
    # -----------------------------
    label = "Face"
    cv2.putText(img, label, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

    # -----------------------------
    # 統計
    # -----------------------------
    count += 1

    # -----------------------------
    # 儲存結果
    # -----------------------------
    save_path = os.path.join(output_dir, "detected_" + filename)
    cv2.imwrite(save_path, img)

# -----------------------------
# 輸出結果
# -----------------------------
print("處理完成")
print("圖片數量:", count)