import re

input_file = "De-1.txt"
output_file = "De-1_fixed.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
for line in lines:
    # Thêm "Câu " trước số đầu dòng (ví dụ: 1. -> Câu 1.)
    fixed_line = re.sub(r"^(\d+)\.", r"Câu \1.", line)
    fixed_lines.append(fixed_line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print("Đã xử lý xong. Kết quả lưu vào:", output_file)
