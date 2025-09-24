import pdfplumber
import re
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_PATH = "matsne-31702-134.pdf"
TXT_PATH = "civil_code.txt"
INDEX_PATH = "faiss_index"

text = ""
with pdfplumber.open(PDF_PATH) as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

parts = re.split(r"(მუხლი\s+\d+)", text)
docs = []
for i in range(1, len(parts), 2):
    header = parts[i].strip()
    body = parts[i+1].strip()
    docs.append(Document(page_content=body, metadata={"article": header}))

with open(TXT_PATH, "w", encoding="utf-8") as f:
    for d in docs:
        f.write(f"{d.metadata['article']}\n{d.page_content}\n\n")

print(f" Created {TXT_PATH} with {len(docs)} articles.")

EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

db = FAISS.from_documents(docs, embeddings)
db.save_local(INDEX_PATH)
print(f" FAISS saved to {INDEX_PATH}")
