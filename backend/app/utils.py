import os
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_embedding(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model = OpenAIEmbeddings()
    return model.embed_documents([text])[0]

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=32)
    return splitter.split_text(text)
