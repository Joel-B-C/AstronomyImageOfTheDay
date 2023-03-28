import requests
import streamlit as st

apikey = "r7iGClOgnduFr1Ev5rFACTRr2Pi8rimsgpFMz0aX"
url = "https://api.nasa.gov/planetary/apod?" \
        f"api_key={apikey}"

response1 = requests.get(url)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
