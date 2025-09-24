import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

INDEX_PATH = "faiss_index"
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

if not os.path.exists(INDEX_PATH):
    raise FileNotFoundError("FAISS ინდექსი არ მოიძებნა. ჯერ გაუშვი ingest.py რომ შექმნას.")

db = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

print(" ინდექსი წარმატებით ჩაიტვირთა!")

query = "რას ამბობს სამოქალაქო კოდექსი ხელშეკრულების შესახებ?"
docs = db.similarity_search(query, k=3)

print("\n შედეგები:")
for i, d in enumerate(docs, 1):
    print(f"{i}. {d.page_content[:300]}...\n")
