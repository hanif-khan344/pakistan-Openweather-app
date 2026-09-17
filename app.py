
import streamlit as st
import requests

st.set_page_config(
    page_title="Pakistan Weather App",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Pakistan Weather App")
st.write("Select a city to view its current weather.")

# City selection
city = st.selectbox(
    "Select City",
    ["Islamabad", "Peshawar"]
)

# OpenWeatherMap API key
API_KEY = st.secrets["OPENWEATHER_API_KEY"]

# Get weather data
def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city + ",PK",
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# Button to show weather
if st.button("Show Weather"):

    weather = get_weather(city)

    if weather:

        temperature = weather["main"]["temp"]
        feels_like = weather["main"]["feels_like"]
        humidity = weather["main"]["humidity"]
        description = weather["weather"][0]["description"]
        wind_speed = weather["wind"]["speed"]

        st.subheader(f"🌍 Weather in {city}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🌡️ Temperature", f"{temperature} °C")
            st.metric("🤗 Feels Like", f"{feels_like} °C")
            st.metric("💧 Humidity", f"{humidity}%")

        with col2:
            st.metric("☁️ Condition", description.title())
            st.metric("💨 Wind Speed", f"{wind_speed} m/s")

    else:
        st.error("Unable to retrieve weather data. Please try again.")
