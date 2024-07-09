import streamlit as st 
import dspy 
import PyPDF2
from dotenv import load_dotenv
load_dotenv()

llm = dspy.Google(model = 'gemini-1.5-flash-latest')

dspy.settings.configure(lm = llm)

class RoastSignature(dspy.Signature):
    """You are professional roaster, you have to roast the user's resume as much as you can based upon the content"""
    content: str = dspy.InputField(desc="containing the user uploaded resume text")
    roast_answer: str = dspy.OutputField(desc="Roast the user's resume as badly as you can")

def main():
    st.set_page_config(
        page_title="Resume Roaster", 
        page_icon="😂",
        layout="wide"
    )
    st.title("Resume Roaster")
    pdf_file = st.file_uploader(label="Upload your resume")
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        content = ""
        for page in range(len(pdf_reader.pages)):
            content += pdf_reader.pages[page].extract_text()
        roast_resume = dspy.ChainOfThought(signature=RoastSignature)
        roast = roast_resume(content=content).roast_answer 
        st.markdown(roast)


if __name__=='__main__':
    main()
