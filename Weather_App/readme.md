This is a Streamlit app that can be used to find the current weather in any city.

To use the app, first clone the repository and install the dependencies. Then, run the app by executing the following command:

```
streamlit run weather.py
```

The app will ask you to enter the name of a city. Once you have entered the city name, the app will display the current weather conditions, including the temperature, humidity, and weather icon.

The app uses the OpenWeatherMap API to get the weather data. The API key is stored in the `API_KEY` variable at the top of the `weather.py` file.

The `convert_to_celcius()` function converts the temperature from Kelvin to Celsius.

The `find_current_weather()` function makes a request to the OpenWeatherMap API and returns the current weather conditions for the specified city.

The `main()` function is the entry point for the app. It displays a header and a text input field for the city name. When the user clicks the `Find` button, the `find_current_weather()` function is called and the current weather conditions are displayed.

The `col1`, `col2`, and `col3` variables are used to create three columns on the Streamlit page. The `st.metric()` function is used to display metrics in each column. The `st.write()` function is used to display the general weather conditions and the weather icon.