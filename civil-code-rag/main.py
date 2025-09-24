from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

embedding_model = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

with open("civil_code.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n", "მუხლი"]
)
docs = splitter.split_text(text)

db = FAISS.from_texts(docs, embeddings)
db.save_local("faiss_index")
print(" FAISS ვექტორული ბაზა შექმნილია!")
