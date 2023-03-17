import streamlit as st
import requests
from streamlit_lottie import st_lottie
import requests
from multiprocessing import Process
import time

body = st.container()

placeholder = st.empty()

with body:
    st.title("Take Care of Your Mushrooms")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(f'<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/2069682/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>',unsafe_allow_html=True,)
    with right_column:
        while True:
            with placeholder.container():
                response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=2')
                prev = float(response.json()["feeds"][0]["field3"])
                recent = float(response.json()["feeds"][1]["field3"])
                delta = recent - prev
                st.metric("Soil Moisture level", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                time.sleep(1)
            placeholder.empty()
