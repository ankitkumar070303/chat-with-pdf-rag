import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from google import genai

# Load environment
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Chat with PDF (Gemini)", layout="wide")
st.title("📄 Chat with your PDF (Gemini)")

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t
    return text

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100
    )
    return splitter.split_text(text)

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(chunks, embeddings)

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    text = read_pdf(pdf)
    chunks = split_text(text)
    vectorstore = create_vector_store(chunks)

    question = st.text_input("Ask a question")

    if question:
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(question)
        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
Answer using ONLY the context below.
If not found, say "Not found in document".

Context:
{context}

Question:
{question}
"""

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        st.write(response.text)