# Motor and Sensor Control on Arduino Raspberry Pi and ESP
<a href="https://github.com/GiorgioCitterio/Motor-and-Sensor-Control-on-Arduino-Raspberry-Pi-and-ESP/blob/main/README.md">README.us🇺🇸</a>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Mosquitto](https://img.shields.io/badge/mosquitto-%233C5280.svg?style=for-the-badge&logo=eclipsemosquitto&logoColor=white)
![Zigbee](https://img.shields.io/badge/zigbee-%23EB0443.svg?style=for-the-badge&logo=zigbee&logoColor=white)
![Amazon Alexa](https://img.shields.io/badge/amazon%20alexa-52b5f7?style=for-the-badge&logo=amazon%20alexa&logoColor=white)

---
## tps_GiorgioCitterio_UmbertoColombo_2022_2023
### Table of Contents
- Activity 1: <a  href="#serard">Serial Communication on Arduino</a>
- Activity 2: <a  href="#serpy">Serial Communication with Python and Arduino</a>
- Activity 3: <a  href="#isoosi">Communication with ISO/OSI Model Packet</a>
- Activity 4: <a  href="#guisensatt">Sensor/Actuator Control via GUI (Python)</a>
- Activity 5: <a  href="#sensjson">Storing Sensor Data in a JSON File</a>
- Activity 7: <a  href="#websens">Making Sensor Data Available on the Web</a>
- Activity 8: <a  href="#webatt">Motor Control via Web Browser</a>
- Activity 9: <a  href="#initrasp">Installation and Importing Programs on Raspberry Pi</a>
- Activity 10: <a  href="#rf24">Sending Packets via RF24 Radio Module</a>
- Activity 11: <a  href="#sensattrasp">Controlling Motor and Sensor from Raspberry Pi</a>
- Activity 12: <a  href="#mqtt">Using MQTT for IoT Device Communication</a>
- Activity 13: <a  href="#mqttesp">Using MQTT with ESP8266</a>
- Activity 14: <a  href="#alexa">Controlling Sensor and Actuator with Alexa</a>
- Activity 15: <a  href="#ble">Using BLE for Environment Control</a>
---

For library installation on [Linux systems](lib.md).

---

# Activity 1: <a name="serard"></a>

**Activity Report 1**: [Serial Communication on Arduino](01_TrasmissioneSerialeArduino/01_TrasmissioneSerialeArduino_Relazione.pdf).

Exploration of serial communication on Arduino.

---

# Activity 2: <a name="serpy"></a>

**Activity Report 2**: [Serial Communication with Python and Arduino](02_Python-2-Seriale/02_Python_2_Seriale_Relazione.pdf).

Communication between a Python application running on Windows and a sensor (potentiometer) and an actuator (L293D motor) connected to an Arduino.

To communicate with the serial port using Python, the *serial* library is used, which can be installed on Windows with the following command:
```
py -m pip install pyserial
```

Official documentation for the [serial library](https://pyserial.readthedocs.io/en/latest/pyserial.html).

---

# Activity 3: <a name="isoosi"></a>

**Activity Report 3**: [Communication with ISO/OSI Model Packet](03_Python-3-Pacchetto_livello_3_7_del%20modello_ISO-OSI_su_seriale/03_Python_3_Pacchetto_livello_3_7_modello_ISOOSI_su_seriale_Relazione.pdf).

Reorganizing the message format exchanged between sensors/actuators and the Python application to work with an RF24 module, which has a payload of 32 bytes.

The *struct* library in Python is used to create these packets.

Official documentation for the [struct library

](https://docs.python.org/3/library/struct.html).

---

# Activity 4: <a name="guisensatt"></a>

**Activity Report 4**: [Sensor/Actuator Control via GUI (Python)](04_Python-4-GUI/04_Python_4_GUI_Relazione.pdf).

Controlling a sensor and actuator through a GUI using Python. Three different programs for the actuator and three for the sensor.

The GUI (Graphical User Interface) is created using the *tkinter* library, which can be installed for most users with the following command:
```
py -m pip install tkinter
```

Official documentation for the [tkinter library](https://docs.python.org/3/library/tk.html).

In the latest version of the sensor program, the *matplotlib* library is used to create a graph. It can be installed (on Windows) with the following command:
```
py -m pip install matplotlib
```

Official documentation for the [matplotlib library](https://matplotlib.org/).

---

# Activity 5: <a name="sensjson"></a>

**Activity Report 5**: [Storing Sensor Data in a JSON File](05_Python-5-JSON/05_Python_5_JSON_Relazione.pdf).

Storing sensor data received in a JSON file for later use in client/server data exchange.

To write to a JSON file from Python, the *json* library, which is already available in Python, is used.

Official documentation for the [json library](https://docs.python.org/3/library/json.html).

---

# Activity 7: <a name="websens"></a>

**Activity Report 7**: [Making Sensor Data Available on the Web](07_Python-7-Flask/07_Python_7_Flask_Relazione.pdf).

Making sensor data stored in a JSON file available on the web using Flask and tunneling.

To create the web server, the *Flask* library is used, which can be installed (on Windows) with the following command:
```
py -m pip install Flask
```

Official documentation for the [Flask library](https://flask.palletsprojects.com/en/2.2.x/).

---

# Activity 8: <a name="webatt"></a>

**Activity Report 8**: [Motor Control via Web Browser](08_Python-8-Form/08_Python_8_Form_Relazione.pdf).

Sending data from a web browser to a Flask application to control the motor.

---
# Activity 9<a name="initrasp"></a>

Installation and program importation on **Raspberry Pi**.

---

# Activity 10<a name="rf24"></a>

**Activity Report 10**: [Sending Packets via RF24 Radio Module](10_RF24-Packet-Arduino/10_RF24_Packet_Arduino_Report.pdf).

How to send packets created in the "Layer 3 Packet - Serial" phase using the **nRF24L01+** radio module.

To use the **nRF24L01+** radio module, you need to import the *RF24* library on Arduino.

Official documentation for the [RF24 library](https://nrf24.github.io/RF24/classRF24.html).
[RF24 GitHub](https://github.com/bjarne-hansen/py-nrf24).

---

# Activity 11<a name="sensattrasp"></a>

**Activity Report 11**: [Motor and Sensor Control from Raspberry Pi](11_RF24-Packet-Raspberry/11_RF24-Packet-Raspberry_Report.pdf).

How to display sensor data and control the motor through a Flask server running on **Raspberry Pi**, which communicates with the two Arduinos using the **nRF24L01+** radio module.

To control the **GPIO** pins on **Raspberry Pi**, you need to install the *pigpiod* library using the following command:
```
sudo apt-get install pigpiod
```

To interface with the **RF24** radio module from Python, you need to import the *nrf24* library using the following command:
```
python3 -m pip install nrf24
```

---

# Activity 12<a name="mqtt"></a>

**Activity Report 12**: [Using MQTT for IoT Device Communication](12_Cloud-MQTT/12_Cloud_MQTT_Report.pdf).

How to use the MQTT protocol to communicate between IoT devices, including through apps.

To use MQTT with Python, you need to import the *paho-mqtt* library using the following command:
```
python3 -m pip install paho-mqtt
```

---

# Activity 13<a name="mqttesp"></a>

**Activity Report 13**: [Using MQTT with ESP8266](13_Cloud-MQTT-ESP8266/13_Cloud_MQTT_ESP8266_Report.pdf).

How to use MQTT for message exchange between IoT devices directly connected to ESP8266 with WiFi connectivity.

You will need to add the board manager to the Arduino IDE to manage the ESP8266.

[Tutorial for installation](https://www.vincenzov.net/tutorial/ESP/ESP8266/Arduino-IDE.htm).

---

# Activity 14<a name="alexa"></a>

TODO: How to control the sensor and actuator using Alexa.

---

# Activity 15<a name="ble"></a>

**Activity Report 15**: [Using BLE for Environment Control](15_Cloud_BLE/15_Cloud_BLE_Report.pdf).

How to use ESP32 to create devices that utilize the Bluetooth Low Energy (BLE) protocol for communication.

To control the ESP32 from the Arduino IDE, you will need to add the board manager as previously done for the ESP8266.

