import os
from io import BytesIO
from docx import Document
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

def process_input(input_type, input_data):
    """Processes different input types and returns a vectorstore."""
    from vectorstore_manager import create_vectorstore

    loader = None
    if input_type == "Link":
        loader = WebBaseLoader(input_data)
        documents = loader.load()
    elif input_type == "PDF":
        pdf_reader = PdfReader(input_data if isinstance(input_data, BytesIO) else BytesIO(input_data.read()))
        text = "".join([page.extract_text() for page in pdf_reader.pages])
        documents = text
    elif input_type == "Text":
        documents = input_data
    elif input_type == "DOCX":
        doc = Document(input_data if isinstance(input_data, BytesIO) else BytesIO(input_data.read()))
        documents = "\n".join([para.text for para in doc.paragraphs])
    elif input_type == "TXT":
        text = input_data.read().decode('utf-8') if isinstance(input_data, BytesIO) else str(input_data.read().decode('utf-8'))
        documents = text
    else:
        raise ValueError("Unsupported input type")

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    if input_type == "Link":
        texts = [str(doc.page_content) for doc in text_splitter.split_documents(documents)]
    else:
        texts = text_splitter.split_text(documents)

    return create_vectorstore(texts)
