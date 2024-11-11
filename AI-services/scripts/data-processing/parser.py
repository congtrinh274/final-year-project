import json

# Đọc dữ liệu từ file JSON
with open("cv1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Chuyển đổi dữ liệu sang định dạng mong muốn
output = []
for record in data:
    text = record["text"]
    entities = []

    for label_info in record["label"]:
        for label in label_info["labels"]:
            entities.append([label_info["start"], label_info["end"], label])

    output.append([text, {"entities": entities}])

# Lưu kết quả vào file mới
with open("cv1parsed.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False)

print("Chuyển đổi hoàn tất. File 'output.json' đã được tạo.")
