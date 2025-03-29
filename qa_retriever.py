import os
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import HUGGINGFACE_API_KEY

HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

def answer_question(vectorstore, query):
    """Answers the question based on the provided vectorstore."""
    llm = HuggingFaceEndpoint(
        repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
        token=HUGGINGFACE_API_KEY,
        temperature=0.6
    )
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa({"query": query})