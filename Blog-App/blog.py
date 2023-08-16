import streamlit as st
import replicate 
import os 
import requests
from pexels_api import API 
from random import randint
check = True
RANDOM_NUMBER = randint(0,5)

quotes = [
    ['Technology is best when it brings people together.', '~ Matt Mullengen, Social Media Entrepreneur'],
    ['It has become appallingly obvious that our technology has exceeded our humanity.', '~ Albert Einstein, Physicist'],
    ['It is only when they go wrong that machines remind you how powerful they are.', '~ Clive James, Broadcaster and Journalist'],
    ['The Web as I envisaged it, we have not seen it yet. The future is still so much bigger than the past.','~ Tim Berners-Lee, Inventer of the World Wide Web'],
    ['It is not a faith in technology but in people.', '~ Steve Jobs, Co-founder of Apple'],
    ['The advance of technology is based on making it fit in so that you do not really even notice it, so it is part of everyday life.', '~ Bill Gates, Co-founder of Microsoft']
]


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
    check = False
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




service = st.sidebar.selectbox(label="Select the service you want to use :)", options=['Click it!','LLama 2 Chatbot', 'Text2Image', 'Conversion Calculator', 'Weather', 'Image Search'])




if service=='Click it!' and check:
    st.title(quotes[RANDOM_NUMBER][0])
    st.write(quotes[RANDOM_NUMBER][1])




if service=='Image Search':
    check = False
    API_KEY = 't0Q0bzvEnqf60qO6FutoyISPobJtmtI5dlq20l4ovHlD8RshtsoKEZT4'
    api = API(PEXELS_API_KEY=API_KEY)
    st.title('Search your Image 🔎')
    search = st.text_input('Enter the text', placeholder='Search your image')
    if st.button('Search'):
        api.search(search, page=1, results_per_page=5)
        photos = api.get_entries()
        for photo in photos:
            st.image(photo.original)




if service=='Weather':
    check = False
    API_KEY = 'd03df81fa6320b1f7fbb33c667d4e3c6'


    def convert_to_celcius(temperature_in_kelvin):
        return temperature_in_kelvin-273.15

    def find_current_weather(city):
        base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        weather_data = requests.get(base_url).json()
        try:
            general = weather_data['weather'][0]['main']
            icon_id = weather_data['weather'][0]['icon']
            temperature = round(convert_to_celcius(weather_data['main']['temp']))
            max_temperature = round(convert_to_celcius(weather_data['main']['temp_max']))
            feels_temp = round(convert_to_celcius(weather_data['main']['feels_like']))
            humidity = weather_data['main']['humidity']
            icon = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
        except KeyError:
            st.error('City Not Found')
            st.stop()
        return general, temperature, max_temperature, feels_temp, humidity, icon

    def main():
        st.header("Find the Weather 🌥️")
        city = st.text_input("Enter the city").lower()
        if st.button('Find'):
            general, temperature, max_temperature, feels_temp, humidity, icon = find_current_weather(city)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric('Temperature', str(temperature)+'℃', str(max_temperature-temperature)+'℃')
                st.metric('Feels Like', str(feels_temp)+'℃')
            with col2:
                st.metric('Humidity', str(humidity)+'%')
            with col3:
                st.write(general)
                st.image(icon)

    if __name__=='__main__':
        main()




if service=='Conversion Calculator':
    check = False
    st.title('SGPA, CGPA and Percentage Converter')

    st.subheader('SGPA to CGPA and Percentage')

    option = st.selectbox('Select the option', options=['','Percentage', 'SGPA', 'CGPA'])

    if option=='Percentage':
        marks_obtain = st.number_input('Enter the marks')
        total_marks = st.number_input('Enter total marks')
        if st.button('Submit'):
            percentage = (marks_obtain/total_marks)*100
            st.text(f'Percentage: {percentage}')

    if option=='SGPA':
        percentage = st.number_input('Enter the percentage')
        if st.button('Submit'):
            sgpa = (percentage/10)+0.75
            st.text(f'SGPA: {sgpa}')

    if option=='CGPA':
        try:
            sgpas = []
            sems = st.number_input('Number of semester')
            check = True
            j = 0
            for i in range(int(sems)):
                check = False
                a = st.number_input(f'SGPA of Semester {i+1}')
                sgpas.append(a)
            if st.button('Submit'):
                check = True
            if check:
                st.text(f'CGPA of all {sems} semester: {sum(sgpas)/sems}')
        except:
            pass




if service=='Text2Image':
    Check = False
    with st.sidebar:
        st.title('Text2Image 💬🖼️')
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
        st.markdown("You can make your API Token key from here → [Link](https://replicate.com/)")
    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    text=st.text_area('', placeholder='Type something', height=150)
    if st.button("Generate"):
        frame = replicate.run(
        "stability-ai/sdxl:a00d0b7dcbb9c3fbb34ba87d2d5b46c56969c84a628bf778a7fdaec30b1b99c5",
        input={"prompt": text}
        )
        st.image(frame)
        for image in frame:
            response = requests.get(image)
            if response.status_code == 200:
                image_data = response.content
                btn = st.download_button(
                        ":red[**Download**]", data=image_data, file_name="output_file.png", mime="image/png", use_container_width=True)
                if btn:
                    st.toast("Download complete! Go show it off now!", icon="🥂")
            else:
                st.error(f"Failed to fetch image from {frame}. Error code: {response.status_code}", icon="🚨")




if service=='LLama 2 Chatbot':
    check = False
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

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


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

    if prompt := st.chat_input(disabled=not replicate_api):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

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


hide_st_style = '''
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)
