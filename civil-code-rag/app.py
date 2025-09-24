import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


INDEX_PATH = "faiss_index"
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "bigscience/bloom-560m"

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

db = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
model = AutoModelForCausalLM.from_pretrained(LLM_MODEL)

text_generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1
)

llm = HuggingFacePipeline(pipeline=text_generator)

st.title("️ სამოქალაქო კოდექსის RAG აგენტი (ქართული)")

query = st.text_input(" კითხე რამე სამოქალაქო კოდექსზე:")

if query:
    with st.spinner("მუშაობს..."):
        docs = db.similarity_search(query, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        prompt = f"მომხმარებელი გეკითხება:\n{query}\n\nკონტექსტი სამოქალაქო კოდექსიდან:\n{context}\n\nპასუხი ქართულად:"

        answer = llm.invoke(prompt)

    st.subheader(" პასუხი:")
    st.write(answer)

    st.subheader(" წყაროები:")
    for i, d in enumerate(docs, 1):
        st.markdown(f"**{i}.** {d.page_content[:300]}...")
