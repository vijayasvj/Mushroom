import streamlit as st
import requests
from streamlit_lottie import st_lottie
import requests
from multiprocessing import Process
import time

#st.set_page_config(layout="wide")

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
    #if "my_output" not in st.session_state:
    #    st.session_state.my_output = False

    st.markdown('**Select a room**')
    option = st.selectbox(
        'Select a room',
        ('Room - 1', 'Room - 2', 'Room - 3'), label_visibility="collapsed")
    if option:
        st.markdown('**Choose a sensor**')
        genre = st.radio(
        "Choose a sensor",
        ('Temperature', 'Humidity', 'Soil moisture'), label_visibility="collapsed")
        placeholders = st.empty()
        st.markdown("""---""")
    #st.session_state.my_output = None
    

    #Temperature
    if genre=='Temperature':
        pl1 = st.empty()
        pl2 = st.empty() 
        pl3 = st.empty()
    
    if genre=='Humidity':
        pl1 = st.empty()
        pl2 = st.empty() 
        pl3 = st.empty()
    #Soil moisture
    if genre=='Soil moisture':
        pl1 = st.empty()
        pl2 = st.empty() 
        pl3 = st.empty()
        
    if genre=='Temperature':
        with pl1: 
            left_column, right_column = st.columns([1,1])
            with left_column:
                st.subheader("Temperature of "+ option)
                placeholder = st.empty()
                st.caption("The number below the moisture level values denotes the change with respect to the previous reading.")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                #st.title("The Soil Temperature of "+ option+" is shown here.")
            with right_column:
                st_lottie(temp_lottie, height=200, key="coding")
            

        while True:
            response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
            val = response.json()["feeds"][9]["field1"]
            if val is None:
                for i in range(19):
                    val = response.json()["feeds"][9-i-1]["field1"]
                    if val is None:
                        continue
                    else:
                        break
            if val is None:
                val = prev
            recent = float(val)
            delta = recent - prev
            with placeholder.container():
                st.metric("Temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
            prev = recent

    if genre=='Humidity':
        with pl1: 
            left_column, right_column = st.columns([1,1])
            with left_column:
                st.subheader("Humidity of "+ option)
                placeholder2 = st.empty()
                st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                #st.title("The Soil Temperature of "+ option+" is shown here.")
            with right_column:
                st_lottie(hum_lottie, height=200, key="coding1")
    
        while True:
            response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
            val = response.json()["feeds"][9]["field2"]
            if val is None:
                for i in range(19):
                    val = response.json()["feeds"][9-i-1]["field2"]
                    if val is None:
                        continue
                    else:
                        break
            if val is None:
                val = prev
            recent = float(val)
            delta = recent - prev
            with placeholder2.container():
                st.metric("Soil moisture", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
            prev = recent

    if genre=='Soil moisture':
       
        with pl1:
            left_column, right_column = st.columns(2)
            
            with left_column:
                st.markdown('**Select moisture sensor**')
                s1 = st.checkbox('Soil moisture Sensor 1', value=True)
                s2 = st.checkbox('Soil moisture Sensor 2', value=True)
                s3 = st.checkbox('Soil moisture Sensor 3', value=True)
                s4 = st.checkbox('Soil moisture Sensor 4', value=True)
            with right_column:
                st_lottie(soil_lottie, height=200, key="coding2")

        with pl2:
            soil_col1, soil_col2 = st.columns(2)
            with soil_col1:
                if s1 == True:
                    st.subheader("Reading from Sensor 1")
                    placeholders1 = st.empty()
                    #st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                   
                if s2 == True:
                    st.subheader("Reading from Sensor 2")
                    placeholders2 = st.empty()
                    #st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                   

            with soil_col2:       
                if s3 == True:
                    st.subheader("Reading from Sensor 3")
                    placeholders3 = st.empty()
                    #st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                
                if s4 == True:
                    st.subheader("Reading from Sensor 4")
                    placeholders4 = st.empty()
                    #st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
        
        with pl3:
            st.markdown("The number below the moisture level values denotes the change with respect to the previous reading.")
        
        while True:
            response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
            if s1==True:
                val = response.json()["feeds"][9]["field3"]
                if val is None:
                    for i in range(19):
                        val = response.json()["feeds"][9-i-1]["field3"]
                        if val is None:
                            continue
                        else:
                            break
                if val is None:
                    val = prev
                recent = float(val)
                delta = recent - prev
                with placeholders1.container():
                    st.metric("Soil moisture", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent
            
            if s2==True:
                val = response.json()["feeds"][9]["field4"]
                if val is None:
                    for i in range(19):
                        val = response.json()["feeds"][9-i-1]["field4"]
                        if val is None:
                            continue
                        else:
                            break
                if val is None:
                    val = prev
                recent = float(val)
                delta = recent - prev
                with placeholders2.container():
                    st.metric("Soil moisture", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent

            if s3==True:
                val = response.json()["feeds"][9]["field5"]
                if val is None:
                    for i in range(19):
                        val = response.json()["feeds"][9-i-1]["field5"]
                        if val is None:
                            continue
                        else:
                            break
                if val is None:
                    val = prev
                recent = float(val)
                delta = recent - prev
                with placeholders3.container():
                    st.metric("Soil moisture", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent

            if s4==True:
                val = response.json()["feeds"][9]["field6"]
                if val is None:
                    for i in range(19):
                        val = response.json()["feeds"][9-i-1]["field6"]
                        if val is None:
                            continue
                        else:
                            break
                if val is None:
                    val = prev
                recent = float(val)
                delta = recent - prev
                with placeholders4.container():
                    st.metric("Soil moisture", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent
