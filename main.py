import streamlit as st
import requests
from streamlit_lottie import st_lottie
import requests
from multiprocessing import Process
import time
from email.message import EmailMessage
import smtplib
import time


msg = EmailMessage()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("vijay@anywarelabs.com", "wiujrvpkmvikujky")


rj1 = requests.get('http://13.235.65.171:8080/mushroom_get')
lowtemp1 = float(rj1.json()["data"][0]["room1"][0]) 
hightemp1 = float(rj1.json()["data"][0]["room1"][1])
lowhum1 = float(rj1.json()["data"][0]["room1"][2])
highhum1 = float(rj1.json()["data"][0]["room1"][3])
lowsoiltemp1 = float(rj1.json()["data"][0]["room1"][4])
highsoiltemp1 = float(rj1.json()["data"][0]["room1"][5])


rj2 = requests.get('http://13.235.65.171:8080/mushroom_get')
lowtemp2 = float(rj2.json()["data"][0]["room2"][0]) 
hightemp2 = float(rj2.json()["data"][0]["room2"][1])
lowhum2 = float(rj2.json()["data"][0]["room2"][2])
highhum2 = float(rj2.json()["data"][0]["room2"][3])
lowsoiltemp2 = float(rj2.json()["data"][0]["room2"][4])
highsoiltemp2 = float(rj2.json()["data"][0]["room2"][5])

rj3 = requests.get('http://13.235.65.171:8080/mushroom_get')
lowtemp3 = float(rj3.json()["data"][0]["room3"][0]) 
hightemp3 = float(rj3.json()["data"][0]["room3"][1])
lowhum3 = float(rj3.json()["data"][0]["room3"][2])
highhum3 = float(rj3.json()["data"][0]["room3"][3])
lowsoiltemp3 = float(rj3.json()["data"][0]["room3"][4])
highsoiltemp3 = float(rj3.json()["data"][0]["room3"][5])

rj4 = requests.get('http://13.235.65.171:8080/mushroom_get')
lowtemp4 = float(rj4.json()["data"][0]["room4"][0]) 
hightemp4 = float(rj4.json()["data"][0]["room4"][1])
lowhum4 = float(rj4.json()["data"][0]["room4"][2])
highhum4 = float(rj4.json()["data"][0]["room4"][3])
lowsoiltemp4 = float(rj4.json()["data"][0]["room4"][4])
highsoiltemp4 = float(rj4.json()["data"][0]["room4"][5])

#st.set_page_config(layout="wide")
def checkandmail():
    msg = ""
    mess = ""
    room1 = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?api_key=HEXPBNQ6XQK0QXCA&results=10')
    r1t1 = room1.json()["feeds"][9]["field1"]
    if r1t1 is None:
        for i in range(9):
            r1t1 = room1.json()["feeds"][9-i-1]["field1"]
            if r1t1 is None:
                r1t1 = 0
                continue
            else:
                break
    r1h1 = room1.json()["feeds"][9]["field2"]
    if r1h1 is None:
        for i in range(9):
            r1h1 = room1.json()["feeds"][9-i-1]["field2"]
            if r1h1 is None:
                r1h1 = 0
                continue
            else:
                break
    r1s1 = room1.json()["feeds"][9]["field3"]
    if r1s1 is None:
        for i in range(9):
            r1s1 = room1.json()["feeds"][9-i-1]["field3"]
            if r1s1 is None:
                r1s1 = 0
                continue
            else:
                break
    r1s2 = room1.json()["feeds"][9]["field4"]
    if r1s2 is None:
        for i in range(9):
            r1s2 = room1.json()["feeds"][9-i-1]["field4"]
            if r1s2 is None:
                r1s2 = 0
                continue
            else:
                break
    r1s3 = room1.json()["feeds"][9]["field5"]
    if r1s3 is None:
        for i in range(9):
            r1s3 = room1.json()["feeds"][9-i-1]["field5"]
            if r1s3 is None:
                r1s3 = 0
                continue
            else:
                break
    r1s4 = room1.json()["feeds"][9]["field6"]
    if r1s4 is None:
        for i in range(9):
            r1s4 = room1.json()["feeds"][9-i-1]["field6"]
            if r1s4 is None:
                r1s4 = 0
                continue
            else:
                break

    room2 = requests.get('https://api.thingspeak.com/channels/2089928/feeds.json?api_key=HY5F6V582XR5HDB9&results=10')
    r2t1 = room2.json()["feeds"][9]["field1"]
    if r2t1 is None:
        for i in range(9):
            r2t1 = room2.json()["feeds"][9-i-1]["field1"]
            if r2t1 is None:
                r2t1 = 0
                continue
            else:
                break
    r2h1 = room2.json()["feeds"][9]["field2"]
    if r2h1 is None:
        for i in range(9):
            r2h1 = room2.json()["feeds"][9-i-1]["field2"]
            if r2h1 is None:
                r2h1 = 0
                continue
            else:
                break
    r2s1 = room2.json()["feeds"][9]["field3"]
    if r2s1 is None:
        for i in range(9):
            r2s1 = room2.json()["feeds"][9-i-1]["field3"]
            if r2s1 is None:
                r2s1 = 0
                continue
            else:
                break
    r2s2 = room2.json()["feeds"][9]["field4"]
    if r2s2 is None:
        for i in range(9):
            r2s2 = room2.json()["feeds"][9-i-1]["field4"]
            if r2s2 is None:
                r2s2 = 0
                continue
            else:
                break
    r2s3 = room2.json()["feeds"][9]["field5"]
    if r2s3 is None:
        for i in range(9):
            r2s3 = room2.json()["feeds"][9-i-1]["field5"]
            if r2s3 is None:
                r2s3 = 0
                continue
            else:
                break
    r2s4 = room2.json()["feeds"][9]["field6"]
    if r2s4 is None:
        for i in range(9):
            r2s4 = room2.json()["feeds"][9-i-1]["field6"]
            if r2s4 is None:
                r2s4 = 0
                continue
            else:
                break

    room3 = requests.get('https://api.thingspeak.com/channels/2089930/feeds.json?api_key=BIWYSFRQM8OXCR8K&results=10')
    r3t1 = room3.json()["feeds"][9]["field1"]
    if r3t1 is None:
        for i in range(9):
            r3t1 = room3.json()["feeds"][9-i-1]["field1"]
            if r3t1 is None:
                r3t1 = 0
                continue
            else:
                break
    r3h1 = room3.json()["feeds"][9]["field2"]
    if r3h1 is None:
        for i in range(9):
            r3h1 = room3.json()["feeds"][9-i-1]["field2"]
            if r3h1 is None:
                r3h1 = 0
                continue
            else:
                break
    r3s1 = room3.json()["feeds"][9]["field3"]
    if r3s1 is None:
        for i in range(9):
            r3s1 = room3.json()["feeds"][9-i-1]["field3"]
            if r3s1 is None:
                r3s1 = 0
                continue
            else:
                break
    r3s2 = room3.json()["feeds"][9]["field4"]
    if r3s2 is None:
        for i in range(9):
            r3s2 = room3.json()["feeds"][9-i-1]["field4"]
            if r3s2 is None:
                r3s2 = 0
                continue
            else:
                break
    r3s3 = room3.json()["feeds"][9]["field5"]
    if r3s3 is None:
        for i in range(9):
            r3s3 = room3.json()["feeds"][9-i-1]["field5"]
            if r3s3 is None:
                r3s3 = 0
                continue
            else:
                break
    r3s4 = room3.json()["feeds"][9]["field6"]
    if r3s4 is None:
        for i in range(9):
            r3s4 = room3.json()["feeds"][9-i-1]["field6"]
            if r3s4 is None:
                r3s4 = 0
                continue
            else:
                break

    room4 = requests.get('https://api.thingspeak.com/channels/2089939/feeds.json?api_key=MQSING4KWTN77OAX&results=10')
    r4t1 = room4.json()["feeds"][9]["field1"]
    if r4t1 is None:
        for i in range(9):
            r4t1 = room4.json()["feeds"][9-i-1]["field1"]
            if r4t1 is None:
                r4t1 = 0
                continue
            else:
                break
    r4h1 = room4.json()["feeds"][9]["field2"]
    if r4h1 is None:
        for i in range(9):
            r4h1 = room4.json()["feeds"][9-i-1]["field2"]
            if r4h1 is None:
                r4h1 = 0
                continue
            else:
                break
    r4s1 = room4.json()["feeds"][9]["field3"]
    if r4s1 is None:
        for i in range(9):
            r4s1 = room4.json()["feeds"][9-i-1]["field3"]
            if r4s1 is None:
                r4s1 = 0
                continue
            else:
                break
    r4s2 = room4.json()["feeds"][9]["field4"]
    if r4s2 is None:
        for i in range(9):
            r4s2 = room4.json()["feeds"][9-i-1]["field4"]
            if r4s2 is None:
                r4s2 = 0
                continue
            else:
                break
    r4s3 = room4.json()["feeds"][9]["field5"]
    if r4s3 is None:
        for i in range(9):
            r4s3 = room4.json()["feeds"][9-i-1]["field5"]
            if r4s3 is None:
                r4s3 = 0
                continue
            else:
                break
    r4s4 = room4.json()["feeds"][9]["field6"]
    if r4s4 is None:
        for i in range(9):
            r4s4 = room4.json()["feeds"][9-i-1]["field6"]
            if r4s4 is None:
                r4s4 = 0
                continue
            else:
                break

    '''room5 = requests.get('https://api.thingspeak.com/channels/2089940/feeds.json?api_key=AJWARVB1ARI0SGAS&results=10')
    r5t1 = room5.json()["feeds"][9]["field1"]
    if r5t1 is None:
        for i in range(9):
            r5t1 = room5.json()["feeds"][9-i-1]["field1"]
            if r5t1 is None:
                continue
            else:
                break
    r5h1 = room5.json()["feeds"][9]["field2"]
    if r5h1 is None:
        for i in range(9):
            r5h1 = room5.json()["feeds"][9-i-1]["field2"]
            if r5h1 is None:
                continue
            else:
                break
    r5s1 = room5.json()["feeds"][9]["field3"]
    if r5s1 is None:
        for i in range(9):
            r5s1 = room5.json()["feeds"][9-i-1]["field3"]
            if r5s1 is None:
                continue
            else:
                break
    r5s2 = room5.json()["feeds"][9]["field4"]
    if r5s2 is None:
        for i in range(9):
            r5s2 = room5.json()["feeds"][9-i-1]["field4"]
            if r5s2 is None:
                continue
            else:
                break
    r5s3 = room5.json()["feeds"][9]["field5"]
    if r5s3 is None:
        for i in range(9):
            r5s3 = room5.json()["feeds"][9-i-1]["field5"]
            if r5s3 is None:
                continue
            else:
                break
    r5s4 = room5.json()["feeds"][9]["field6"]
    if r5s4 is None:
        for i in range(9):
            r5s4 = room5.json()["feeds"][9-i-1]["field6"]
            if r5s4 is None:
                continue
            else:
                break'''
    i = 1
    if float(r1t1)>hightemp1 or float(r1h1)<lowhum1 or float(r1h1)>highhum1 or float(r1s1)>highsoiltemp1 or float(r1s2)>highsoiltemp1 or float(r1s3)>highsoiltemp1 or float(r1s4)>highsoiltemp1:
        i = i * 0
        msg = msg + "Room-1 "
        if float(r1t1)>hightemp1:
            mess = mess + "In Room-1, check room temperature, "
        if float(r1h1)<lowhum1 or float(r1h1)>highhum1:
            mess = mess + "In Room-1, check room humidity, "
        if float(r1s1)>highsoiltemp1 or float(r1s2)>highsoiltemp1 or float(r1s3)>highsoiltemp1 or float(r1s4)>highsoiltemp1:
            mess = mess + "In Room-1, check all soil temperatures, "
    if float(r2t1)>hightemp2 or float(r2h1)<lowhum2 or float(r2h1)>highhum2 or float(r2s1)>highsoiltemp2 or float(r2s2)>highsoiltemp2 or float(r2s3)>highsoiltemp2 or float(r2s4)>highsoiltemp2:
        i = i * 0
        msg = msg + "Room-2 "
        if float(r2t1)>hightemp2:
            mess = mess + "In Room-2, check room temperature, "
        if float(r2h1)<lowhum2 or float(r2h1)>highhum2:
            mess = mess + "In Room-2, check room humidity, "
        if float(r2s1)>highsoiltemp2 or float(r2s2)>highsoiltemp2 or float(r2s3)>highsoiltemp2 or float(r2s4)>highsoiltemp2:
            mess = mess + "In Room-2, check all soil temperatures, "
    if float(r3t1)>hightemp3 or float(r3h1)<lowhum3 or float(r3h1)>highhum3 or float(r3s1)>highsoiltemp3 or float(r3s2)>highsoiltemp3 or float(r3s3)>highsoiltemp3 or float(r3s4)>highsoiltemp3:
        i = i * 0
        msg = msg + "Room-3 "
        if float(r3t1)>hightemp3:
            mess = mess + "In Room-3, check room temperature, "
        if float(r3h1)<lowhum3 or float(r3h1)>highhum3:
            mess = mess + "In Room-3, check room humidity, "
        if float(r3s1)>highsoiltemp3 or float(r3s2)>highsoiltemp3 or float(r3s3)>highsoiltemp3 or float(r3s4)>highsoiltemp3:
            mess = mess + "In Room-3, check all soil temperatures, "
    if float(r4t1)>hightemp4 or float(r4h1)<lowhum4 or float(r4h1)>highhum4 or float(r4s1)>highsoiltemp4 or float(r4s2)>highsoiltemp4 or float(r4s3)>highsoiltemp4 or float(r4s4)>highsoiltemp4:
        i = i * 0
        msg = msg + "Room-4 "
        if float(r4t1)>hightemp4:
            mess = mess + "In Room-4, check room temperature, "
        if float(r4h1)<lowhum4 or float(r4h1)>highhum4:
            mess = mess + "In Room-4, check room humidity, "
        if float(r4s1)>highsoiltemp4 or float(r4s2)>highsoiltemp4 or float(r4s3)>highsoiltemp4 or float(r4s4)>highsoiltemp4:
            mess = mess + "In Room-4, check all soil temperatures, "
    '''if r5t1>hightemp or r5h1<lowhum or r5h1>highhum or r5s1>highsoiltemp or r5s2>highsoiltemp or r5s3>highsoiltemp or r5s4>highsoiltemp:
        msg['Subject'] = msg['Subject'] + "Room-5 "
        if r5t1>hightemp:
            mess = mess + "In Room-5, check room temperature. "
        if r5h1<lowhum or r5h1>highhum:
            mess = mess + "In Room-5, check room humidity"
        if r5s1>highsoiltemp or r5s2>highsoiltemp or r5s3>highsoiltemp or r5s4>highsoiltemp:
            mess = mess + "In Room-5, check all soil temperatures"'''
    if i == 0:
        print(msg)
        print(mess)
        jason={"title":msg,"message":mess}
        re = requests.get(url = "http://13.235.65.171:8080/trigger_notifi", json = jason)
        print(re)
        


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

with st.sidebar:
    st.subheader("Change your thresholds")
    st.sidebar.info('The notifications will be send to Android mobiles who have our APK installed already')
    st.markdown("""---""")
    optionsr = st.selectbox(
        'Settings for room',
        ('Room - 1', 'Room - 2', 'Room - 3', 'Room - 4'), label_visibility="collapsed")
    if optionsr == 'Room - 1':
        normtemps1 = st.slider('Select a range of normal room - 1 temperature',0.0, 100.0, (lowtemp1, hightemp1))
        normhums1 = st.slider('Select a range of normal room- 1 humidity',0.0, 100.0, (lowhum1, highhum1))
        normsoiltemps1 = st.slider('Select a range of normal room - 1 soil temperature',0.0, 100.0, (lowsoiltemp1, highsoiltemp1))
        save1 = st.button("Save thresholds")
        if save1 == True:
            st.write("New thresholds updated for room 1")
            st.caption("In case of emergency, alerts will be sent to your mail ID.")
            lowtemp1 = normtemps1[0]
            hightemp1 = normtemps1[1]
            lowhum1 = normhums1[0]
            highhum1 = normhums1[1]
            lowsoiltemp1 = normsoiltemps1[0]
            highsoiltemp1 = normsoiltemps1[1]
            real_data={
                        "project":"mushroom",
                            "room1": [lowtemp1, hightemp1, lowhum1, highhum1, lowsoiltemp1, highsoiltemp1]}
            r = requests.post(url = "http://13.235.65.171:8080/mushroom_room1", json = real_data)
            time.sleep(1)
            save1 = False
    
    if optionsr == 'Room - 2':
        
        normtemps2 = st.slider('Select a range of normal room - 2 temperature',0.0, 100.0, (lowtemp2, hightemp2))
        normhums2 = st.slider('Select a range of normal room- 2 humidity',0.0, 100.0, (lowhum2, highhum2))
        normsoiltemps2 = st.slider('Select a range of normal room - 2 soil temperature',0.0, 100.0, (lowsoiltemp2, highsoiltemp2))
        save2 = st.button("Save thresholds")
        if save2 == True:
            st.write("New thresholds updated for room 2")
            st.caption("In case of emergency, alerts will be sent to your mail ID.")
            lowtemp2 = normtemps2[0]
            hightemp2 = normtemps2[1]
            lowhum2 = normhums2[0]
            highhum2 = normhums2[1]
            lowsoiltemp2 = normsoiltemps2[0]
            highsoiltemp2 = normsoiltemps2[1]
            real_data={
                        "project":"mushroom",
                            "room2": [lowtemp2, hightemp2, lowhum2, highhum2, lowsoiltemp2, highsoiltemp2]}
            r = requests.post(url = "http://13.235.65.171:8080/mushroom_room2", json = real_data)
            time.sleep(1)
            save2 = False
    if optionsr == 'Room - 3':
        normtemps3 = st.slider('Select a range of normal room - 3 temperature',0.0, 100.0, (lowtemp3, hightemp3))
        normhums3 = st.slider('Select a range of normal room- 3 humidity',0.0, 100.0, (lowhum3, highhum3))
        normsoiltemps3 = st.slider('Select a range of normal room - 3 soil temperature',0.0, 100.0, (lowsoiltemp3, highsoiltemp3))
        save3 = st.button("Save thresholds")
        if save3 == True:
            st.write("New thresholds updated for room 3")
            st.caption("In case of emergency, alerts will be sent to your mail ID.")
            lowtemp3 = normtemps3[0]
            hightemp3 = normtemps3[1]
            lowhum3 = normhums3[0]
            highhum3 = normhums3[1]
            lowsoiltemp3 = normsoiltemps3[0]
            highsoiltemp3 = normsoiltemps3[1]
            real_data={
                        "project":"mushroom",
                            "room3": [lowtemp3, hightemp3, lowhum3, highhum3, lowsoiltemp3, highsoiltemp3]}
            r = requests.post(url = "http://13.235.65.171:8080/mushroom_room3", json = real_data)
            time.sleep(1)
            save3 = False
    if optionsr == 'Room - 4':
        normtemps4 = st.slider('Select a range of normal room - 4 temperature',0.0, 100.0, (lowtemp4, hightemp4))
        normhums4 = st.slider('Select a range of normal room- 4 humidity',0.0, 100.0, (lowhum4, highhum4))
        normsoiltemps4 = st.slider('Select a range of normal room - 4 soil temperature',0.0, 100.0, (lowsoiltemp4, highsoiltemp4))
        save4 = st.button("Save thresholds")
        if save4 == True:
            st.write("New thresholds updated for room 4")
            st.caption("In case of emergency, alerts will be sent to your mail ID.")
            lowtemp4 = normtemps4[0]
            hightemp4 = normtemps4[1]
            lowhum4 = normhums4[0]
            highhum4 = normhums4[1]
            lowsoiltemp4 = normsoiltemps4[0]
            highsoiltemp4 = normsoiltemps4[1]
            real_data={
                        "project":"mushroom",
                            "room4": [lowtemp4, hightemp4, lowhum4, highhum4, lowsoiltemp4, highsoiltemp4]}
            r = requests.post(url = "http://13.235.65.171:8080/mushroom_room4", json = real_data)
            time.sleep(1)
            save4 = False


with body:
    st.title("Take Care of Your Mushrooms")
    #if "my_output" not in st.session_state:
    #    st.session_state.my_output = False

    st.markdown('**Select a room**')
    option = st.selectbox(
        'Select a room',
        ('Room - 1', 'Room - 2', 'Room - 3', 'Room - 4', 'Composing Room'), label_visibility="collapsed")
    if option:
        st.markdown('**Choose a sensor**')
        genre = st.radio(
        "Choose a sensor",
        ('Temperature', 'Humidity', 'Soil temperature'), label_visibility="collapsed")
        placeholders = st.empty()
        st.markdown("""---""")
    #st.session_state.my_output = None
    
    if option == 'Room - 1':
        #Temperature
        if genre=='Temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        
        if genre=='Humidity':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        #Soil temperature
        if genre=='Soil temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
            
        if genre=='Temperature':
            with pl1: 
                left_column, right_column = st.columns([1,1])
                with left_column:
                    st.subheader("Temperature of "+ option)
                    placeholder = st.empty()
                    st.caption("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(temp_lottie, height=200, key="coding")
                

            while True:
                response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?results=10')
                val = response.json()["feeds"][9]["field1"]
                if val is None:
                    for i in range(9):
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
                checkandmail()


        if genre=='Humidity':
            with pl1: 
                left_column, right_column = st.columns([1,1])
                with left_column:
                    st.subheader("Humidity of "+ option)
                    placeholder2 = st.empty()
                    st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(hum_lottie, height=200, key="coding1")
        
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?results=10')
                val = response.json()["feeds"][9]["field2"]
                if val is None:
                    for i in range(9):
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
                    st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent
                checkandmail()

        if genre=='Soil temperature':
        
            with pl1:
                left_column, right_column = st.columns(2)
                
                with left_column:
                    st.markdown('**Select temperature sensor**')
                    s1 = st.checkbox('Soil temperature Sensor 1', value=True)
                    s2 = st.checkbox('Soil temperature Sensor 2', value=True)
                    s3 = st.checkbox('Soil temperature Sensor 3', value=True)
                    s4 = st.checkbox('Soil temperature Sensor 4', value=True)
                with right_column:
                    st_lottie(soil_lottie, height=150, key="coding2")

            with pl2:
                soil_col1, soil_col2 = st.columns(2)
                with soil_col1:
                    if s1 == True:
                        st.subheader("Reading from Sensor 1")
                        placeholders1 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s2 == True:
                        st.subheader("Reading from Sensor 2")
                        placeholders2 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    

                with soil_col2:       
                    if s3 == True:
                        st.subheader("Reading from Sensor 3")
                        placeholders3 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s4 == True:
                        st.subheader("Reading from Sensor 4")
                        placeholders4 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
            
            with pl3:
                st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
            
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2069682/feeds.json?results=10')
                if s1==True:
                    val = response.json()["feeds"][9]["field3"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                
                if s2==True:
                    val = response.json()["feeds"][9]["field4"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s3==True:
                    val = response.json()["feeds"][9]["field5"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s4==True:
                    val = response.json()["feeds"][9]["field6"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent


    if option == 'Room - 2':
        #Temperature
        if genre=='Temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        
        if genre=='Humidity':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        #Soil temperature
        if genre=='Soil temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
            
        if genre=='Temperature':
            with pl1: 
                left_column, right_column = st.columns([1,1])
                with left_column:
                    st.subheader("Temperature of "+ option)
                    placeholder = st.empty()
                    st.caption("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(temp_lottie, height=200, key="coding")
                

            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089928/feeds.json?api_key=HY5F6V582XR5HDB9&results=10')
                val = response.json()["feeds"][9]["field1"]
                if val is None:
                    for i in range(9):
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
                    st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(hum_lottie, height=200, key="coding1")
        
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089928/feeds.json?api_key=HY5F6V582XR5HDB9&results=10')
                val = response.json()["feeds"][9]["field2"]
                if val is None:
                    for i in range(9):
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
                    st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent

        if genre=='Soil temperature':
        
            with pl1:
                left_column, right_column = st.columns(2)
                
                with left_column:
                    st.markdown('**Select temperature sensor**')
                    s1 = st.checkbox('Soil temperature Sensor 1', value=True)
                    s2 = st.checkbox('Soil temperature Sensor 2', value=True)
                    s3 = st.checkbox('Soil temperature Sensor 3', value=True)
                    s4 = st.checkbox('Soil temperature Sensor 4', value=True)
                with right_column:
                    st_lottie(soil_lottie, height=150, key="coding2")

            with pl2:
                soil_col1, soil_col2 = st.columns(2)
                with soil_col1:
                    if s1 == True:
                        st.subheader("Reading from Sensor 1")
                        placeholders1 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s2 == True:
                        st.subheader("Reading from Sensor 2")
                        placeholders2 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    

                with soil_col2:       
                    if s3 == True:
                        st.subheader("Reading from Sensor 3")
                        placeholders3 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s4 == True:
                        st.subheader("Reading from Sensor 4")
                        placeholders4 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
            
            with pl3:
                st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
            
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089928/feeds.json?api_key=HY5F6V582XR5HDB9&results=10')
                if s1==True:
                    val = response.json()["feeds"][9]["field3"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                
                if s2==True:
                    val = response.json()["feeds"][9]["field4"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s3==True:
                    val = response.json()["feeds"][9]["field5"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s4==True:
                    val = response.json()["feeds"][9]["field6"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent


    if option == 'Room - 3':
        #Temperature
        if genre=='Temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        
        if genre=='Humidity':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        #Soil temperature
        if genre=='Soil temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
            
        if genre=='Temperature':
            with pl1: 
                left_column, right_column = st.columns([1,1])
                with left_column:
                    st.subheader("Temperature of "+ option)
                    placeholder = st.empty()
                    st.caption("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(temp_lottie, height=200, key="coding")
                

            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089930/feeds.json?api_key=BIWYSFRQM8OXCR8K&results=10')
                val = response.json()["feeds"][9]["field1"]
                if val is None:
                    for i in range(9):
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
                    st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(hum_lottie, height=200, key="coding1")
        
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089930/feeds.json?api_key=BIWYSFRQM8OXCR8K&results=10')
                val = response.json()["feeds"][9]["field2"]
                if val is None:
                    for i in range(9):
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
                    st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent

        if genre=='Soil temperature':
        
            with pl1:
                left_column, right_column = st.columns(2)
                
                with left_column:
                    st.markdown('**Select temperature sensor**')
                    s1 = st.checkbox('Soil temperature Sensor 1', value=True)
                    s2 = st.checkbox('Soil temperature Sensor 2', value=True)
                    s3 = st.checkbox('Soil temperature Sensor 3', value=True)
                    s4 = st.checkbox('Soil temperature Sensor 4', value=True)
                with right_column:
                    st_lottie(soil_lottie, height=150, key="coding2")

            with pl2:
                soil_col1, soil_col2 = st.columns(2)
                with soil_col1:
                    if s1 == True:
                        st.subheader("Reading from Sensor 1")
                        placeholders1 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s2 == True:
                        st.subheader("Reading from Sensor 2")
                        placeholders2 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    

                with soil_col2:       
                    if s3 == True:
                        st.subheader("Reading from Sensor 3")
                        placeholders3 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s4 == True:
                        st.subheader("Reading from Sensor 4")
                        placeholders4 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
            
            with pl3:
                st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
            
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089930/feeds.json?api_key=BIWYSFRQM8OXCR8K&results=10')
                if s1==True:
                    val = response.json()["feeds"][9]["field3"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                
                if s2==True:
                    val = response.json()["feeds"][9]["field4"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s3==True:
                    val = response.json()["feeds"][9]["field5"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s4==True:
                    val = response.json()["feeds"][9]["field6"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent



    if option == 'Room - 4':
        #Temperature
        if genre=='Temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        
        if genre=='Humidity':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
        #Soil temperature
        if genre=='Soil temperature':
            pl1 = st.empty()
            pl2 = st.empty() 
            pl3 = st.empty()
            
        if genre=='Temperature':
            with pl1: 
                left_column, right_column = st.columns([1,1])
                with left_column:
                    st.subheader("Temperature of "+ option)
                    placeholder = st.empty()
                    st.caption("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(temp_lottie, height=200, key="coding")
                

            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089939/feeds.json?api_key=MQSING4KWTN77OAX&results=10')
                val = response.json()["feeds"][9]["field1"]
                if val is None:
                    for i in range(9):
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
                    st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                    st.write("###")
                    st.write("###")
                    #st.title("The Soil Temperature of "+ option+" is shown here.")
                with right_column:
                    st_lottie(hum_lottie, height=200, key="coding1")
        
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089939/feeds.json?api_key=MQSING4KWTN77OAX&results=10')
                val = response.json()["feeds"][9]["field2"]
                if val is None:
                    for i in range(9):
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
                    st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                prev = recent

        if genre=='Soil temperature':
        
            with pl1:
                left_column, right_column = st.columns(2)
                
                with left_column:
                    st.markdown('**Select temperature sensor**')
                    s1 = st.checkbox('Soil temperature Sensor 1', value=True)
                    s2 = st.checkbox('Soil temperature Sensor 2', value=True)
                    s3 = st.checkbox('Soil temperature Sensor 3', value=True)
                    s4 = st.checkbox('Soil temperature Sensor 4', value=True)
                with right_column:
                    st_lottie(soil_lottie, height=150, key="coding2")

            with pl2:
                soil_col1, soil_col2 = st.columns(2)
                with soil_col1:
                    if s1 == True:
                        st.subheader("Reading from Sensor 1")
                        placeholders1 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s2 == True:
                        st.subheader("Reading from Sensor 2")
                        placeholders2 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    

                with soil_col2:       
                    if s3 == True:
                        st.subheader("Reading from Sensor 3")
                        placeholders3 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
                    
                    if s4 == True:
                        st.subheader("Reading from Sensor 4")
                        placeholders4 = st.empty()
                        #st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
                        #st.title("The Soil Temperature of "+ option+" is shown here.")
            
            with pl3:
                st.markdown("The number below the temperature level values denotes the change with respect to the previous reading.")
            
            while True:
                response = requests.get('https://api.thingspeak.com/channels/2089939/feeds.json?api_key=MQSING4KWTN77OAX&results=10')
                if s1==True:
                    val = response.json()["feeds"][9]["field3"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent
                
                if s2==True:
                    val = response.json()["feeds"][9]["field4"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s3==True:
                    val = response.json()["feeds"][9]["field5"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent

                if s4==True:
                    val = response.json()["feeds"][9]["field6"]
                    if val is None:
                        for i in range(9):
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
                        st.metric("Soil temperature", recent, delta=delta, delta_color="normal", help=None, label_visibility="visible")
                    prev = recent



