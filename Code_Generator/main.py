import streamlit as st 
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os

load_dotenv()

with st.sidebar:
        st.title('API_KEY Generator 🔑')
        openai_api = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai_api.startswith('sk_') and len(openai_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
        st.markdown("You can make your API Token key from here → [Link](https://openai.com/)")

os.environ['OPENAI_API_KEY'] = openai_api

llm = ChatOpenAI(model='gpt-3.5-turbo', api_key=openai_api) # Insert your API KEY here to run the app

code_prompt = PromptTemplate(
    input_variables = ["task", "language"],
    template = "Write a very short {language} function that will {task}"
)

test_prompt = PromptTemplate(
    input_variables = ["language", "task", "code"],
    template = "Write a test for the following {language} function and check if it will {task}: \n{code}"
)

explain_prompt = PromptTemplate(
    input_variables = ["language", "task", "code"],
    template = "Explain very briefly how the following {language} function will {task}: \n{code}"
)

code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")
test_chain = LLMChain(llm=llm, prompt=test_prompt, output_key="test")
explain_chain = LLMChain(llm=llm, prompt=explain_prompt, output_key="explanation")

chain = SequentialChain(
    input_variables = ["task","language"],
    output_variables = ["code","test","explanation"],
    chains = [code_chain, test_chain, explain_chain]
)

st.title("Code Generator")

task = st.text_input('Task', 'print hello world')
language = st.selectbox('Language', ['Python', 'Java', 'C', 'C++'])

if st.button('Generate Code'):
    result = chain({"task": task, "language": language})

    st.subheader('Generated Code')
    st.code(result['code'], language=language.lower())

    st.subheader('Generated Test')
    st.code(result['test'], language=language.lower())

    st.subheader('Explanation of Code')
    st.markdown(result['explanation'])