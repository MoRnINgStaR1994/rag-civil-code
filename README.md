#  RAG Civil Code Chatbot (ქართული)

ეს არის **Retrieval-Augmented Generation (RAG)** ჩეთბოტი, რომელიც გეხმარება **საქართველოს სამოქალაქო კოდექსის** ტექსტზე კითხვების დასმასა და პასუხების მიღებაში ქართულ ენაზე.  
პროექტი იყენებს **FAISS vector store-ს**, **HuggingFace embeddings-ს** და **HuggingFace LLM-ს** ტექსტის დასამუშავებლად.

---

##  ინსტალაცია და გაშვება

პროექტის გასაშვებად გამოიყენე შემდეგი ნაბიჯები:

```bash
# 1. პროექტის კლონირება
git clone https://github.com/yourusername/rag-civil-code.git
cd rag-civil-code

# 2. ვირტუალური გარემოს შექმნა და აქტივაცია
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

# 3. საჭირო ბიბლიოთეკების დაყენება
pip install -r requirements.txt

# 4. მონაცემების ინდეგსირება (სამოქალაქო კოდექსის ტექსტის დამუშავება)
ჯერ გაუშვით ingest.py რომ შექმნას FAISS ინდექსი
python ingest.py

# 5. ტესტი ტერმინალიდან (კითხვის დასმა ინდეგსირებულ მონაცემებზე ტერმინალში)
python query.py

# 6. Streamlit ჩეთბოტის გაშვება
streamlit run app.py
