import pdfplumber
import re

pdf_path = "matsne-31702-134.pdf"
txt_path = "civil_code.txt"

with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

articles = re.split(r"(მუხლი\s+\d+)", text)
civil_code = ""
for i in range(1, len(articles), 2):
    header = articles[i].strip()
    body = articles[i+1].strip()
    civil_code += f"{header} {body}\n\n"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(civil_code)

print(f" civil_code.txt შექმნილია ({len(articles)//2} მუხლი).")
