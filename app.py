import streamlit as st
from text_extractor import process_input
from qa_retriever import answer_question

def main():
    st.title("RAG Q&A Application")
    input_type = st.selectbox("Input Type", ["Link", "PDF", "Text", "DOCX", "TXT"])
    
    if input_type == "Link":
        number_input = st.number_input(min_value=1, max_value=20, step=1, label="Enter the number of Links")
        input_data = []
        for i in range(number_input):
            url = st.sidebar.text_input(f"URL {i+1}")
            input_data.append(url)
    elif input_type == "Text":
        input_data = st.text_input("Enter the text")
    elif input_type == "PDF":
        input_data = st.file_uploader("Upload a PDF file", type=["pdf"])
    elif input_type == "TXT":
        input_data = st.file_uploader("Upload a text file", type=["txt"])
    elif input_type == "DOCX":
        input_data = st.file_uploader("Upload a DOCX file", type=["docx", "doc"])

    if st.button("Proceed"):
        vectorstore = process_input(input_type, input_data)
        st.session_state["vectorstore"] = vectorstore

    if "vectorstore" in st.session_state:
        query = st.text_input("Ask your question")
        if st.button("Submit"):
            answer = answer_question(st.session_state["vectorstore"], query)
            st.write(answer)

if __name__ == "__main__":
    main()


#python -m streamlit run app.py