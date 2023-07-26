import streamlit as st
import requests

API_KEY = 'd03df81fa6320b1f7fbb33c667d4e3c6'


def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin-273.15

def find_current_weather(city):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    weather_data = requests.get(base_url).json()
    # st.json(weather_data)
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
    st.header("Find the Weather")
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