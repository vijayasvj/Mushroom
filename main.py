import streamlit as st
import requests
from streamlit_lottie import st_lottie
import requests
from multiprocessing import Process
import time

body = st.container()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

temp_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_ujecarck.json")
hum_lottie = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_oj6pxozf.json")
soil_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_e3ux72wx.json")
prev = 0.00
placeholder = st.empty()

with body:
    st.title("Take Care of Your Mushrooms")
    import streamlit as st
    option = st.selectbox(
        'Select the ROOM',
        ('Room - 1', 'Room - 2', 'Room - 3'))
    if option:
        genre = st.radio(
        "Choose a sensor",
        ('Temperature', 'Humidity', 'Soil moisture'))
    if genre=='Temperature':
        iou, left_column, right_column = st.columns([1,1,1])
        with iou:
            st.title("The temperature of "+ option+" is shown here.")
        with right_column:
            st_lottie(temp_lottie, height=250, key="coding")
        with left_column:
            while True:
                with placeholder.container():
                    response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
                    val = response.json()["feeds"][9]["field1"]
                    if val is None:
                        for i in range(9):
                            val = response.json()["feeds"][9-i-1]["field1"]
                            if val is None:
                                continue
                            else:
                                break
                    recent = float(val)
                    delta = recent - prev
                    st.metric("Temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                    time.sleep(1)
                placeholder.empty()


    if genre=='Humidity':
        iou, left_column, right_column = st.columns([1,1,1])
        with iou:
            st.title("The Humidity of "+ option+" is shown here.")
        with right_column:
            st_lottie(hum_lottie, height=250, key="coding")
        with left_column:
            while True:
                with placeholder.container():
                    response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
                    val = response.json()["feeds"][9]["field2"]
                    if val is None:
                        for i in range(9):
                            val = response.json()["feeds"][9-i-1]["field2"]
                            if val is None:
                                continue
                            else:
                                break
                    recent = float(val)
                    delta = recent - prev
                    st.metric("Humidity", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                    time.sleep(1)
                placeholder.empty()


    if genre=='Soil moisture':
        iou, left_column, right_column = st.columns([1,1,1])
        with iou:
            st.title("The Soil Temperature of "+ option+" is shown here.")
        with right_column:
            st_lottie(soil_lottie, height=250, key="coding")
        with left_column:
            while True:
                with placeholder.container():
                    response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
                    val = response.json()["feeds"][9]["field3"]
                    if val is None:
                        for i in range(9):
                            val = response.json()["feeds"][9-i-1]["field3"]
                            if val is None:
                                continue
                            else:
                                break
                    recent = float(val)
                    delta = recent - prev
                    st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                    time.sleep(1)
                placeholder.empty()
