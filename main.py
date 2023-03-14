import streamlit as st
import requests
from streamlit_lottie import st_lottie

body = st.container()



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_mwnl7iyc.json")

with body:
    st.title('Temperature and Humidity values')
    st.write('For ROOM-1')
    st.write('These are all dummyt as of now')
    st.write('###')
    #st.write('##')
    st_lottie(lottie, height=250, key="coding")

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("Temperature Sensor")
        st.write(f'<iframe src="https://thingspeak.com/channels/2064592/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>',unsafe_allow_html=True,)
        
    with right_column:
        st.markdown("Humidity Sensor")
        st.write(f'<iframe src="https://thingspeak.com/channels/2064592/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>',unsafe_allow_html=True,)
