import streamlit as st
import replicate 
import os 

st.set_page_config(
    page_title="Blog App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is my personal blog app 😄. This is an *extremely* useful 😉 app for you!"
    }
)


st.sidebar.title("Everything Is Present Here 😎")

if st.sidebar.button("About Me"):
    st.title("Hello 👋, I'm Mayank Goswami")
    st.header("About Me:")
    st.write(
        '''
        →   👦🏻 I am college student pursuing my bachelor's in Computer Science Engineering.\n
        →   👀 My interest is in the field of Data Science and Machine Learning.\n
        →   💡 Currently working with the startup to build the solutions for modern agriculture.\n
        →   🧑🏻‍💻 I also do competitive programming on various platform using Python and C++.\n
        →   😉 That's all about me now you can watch out for services present in this app.
        '''
    )
    st.write("Get in touch with me")
    st.markdown("[![Linkedln](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mayank-goswami-8909961b9/)")
    st.markdown("[![Instagram](https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mayank04102002/)")
    st.markdown("[![Gmail](https://img.shields.io/badge/gmail-%23EE0000.svg?&style=for-the-badge&logo=gmail&logoColor=white)](mailto:mayankgoswami247@gmail.com)")


service = st.sidebar.selectbox(label="Select the service", options=['Click it!','LLama 2 Chatbot'])

if service=='LLama 2 Chatbot':
    with st.sidebar:
        st.title('🦙💬 Llama 2 Chatbot')
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
        st.markdown("You can make your API Token key from here → [Link](https://replicate.com/)")

    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    # Display or clear chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    # Function for generating LLaMA2 response
    # Refactored from <https://github.com/a16z-infra/llama2-chatbot>
    def generate_llama2_response(prompt_input):
        string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
        for dict_message in st.session_state.messages:
            if dict_message["role"] == "user":
                string_dialogue += "User: " + dict_message["content"] + "\\n\\n"
            else:
                string_dialogue += "Assistant: " + dict_message["content"] + "\\n\\n"
        output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
        return output

    # User-provided prompt
    if prompt := st.chat_input(disabled=not replicate_api):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_llama2_response(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)