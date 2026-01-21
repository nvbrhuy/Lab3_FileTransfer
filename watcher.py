import os
import time
import shutil
import csv

# =========================
# Cấu hình đường dẫn (Path)
# =========================
INPUT_DIR = "./input"
PROCESSED_DIR = "./processed"
ERROR_DIR = "./error"


def process_file(filepath):
    print(f"⚡ Found new file: {filepath}")
    filename = os.path.basename(filepath)

    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            print(" --- READING DATA ---")

            for row in reader:
                try:
                    sku = row["sku"]
                    qty = int(row["qty"])  # Có thể gây lỗi nếu qty không phải số

                    # Validation Logic (Kiểm tra dữ liệu bẩn)
                    if qty < 0:
                        raise ValueError(f"Stock cannot be negative: {qty}")

                    print(f" > Updated SKU: {sku} | New Qty: {qty}")
                except ValueError:
                    print("Skipped bad row...")

        # Nếu đọc xong không lỗi → Move sang folder Processed
        shutil.move(filepath, os.path.join(PROCESSED_DIR, filename))
        print(f"✅ Success! Moved to {PROCESSED_DIR}")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

        # Nếu lỗi → Move sang folder Error
        shutil.move(filepath, os.path.join(ERROR_DIR, filename))
        print(f"⚠️ Moved to {ERROR_DIR}")


def start_watching():
    print("👀 Watchdog Service Started... Waiting for files in /input", flush=True)

    while True:
        try:
            # 1. Quét tất cả file trong thư mục Input
            files = os.listdir(INPUT_DIR)
        except Exception as e:
            print(f"❌ Cannot access input directory: {e}")
            time.sleep(5)
            continue

        for file in files:
            # Chỉ xử lý file CSV
            if not file.lower().endswith(".csv"):
                continue

            full_path = os.path.join(INPUT_DIR, file)

            # Đảm bảo là file (không phải folder)
            if not os.path.isfile(full_path):
                continue

            print(f"📥 Detected file: {file}")
            process_file(full_path)

        # 2. Ngủ 5 giây rồi quét tiếp (Polling)
        time.sleep(5)


if __name__ == "__main__":
    start_watching()

