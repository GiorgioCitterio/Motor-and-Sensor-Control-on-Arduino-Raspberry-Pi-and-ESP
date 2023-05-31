# tps_2022_2023
tps_GiorgioCitterio_UmbertoColombo_2022_2023
---
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
---

Per l'installazione delle librerie su sistemi [Linux](lib.md).

---

# Attività 1

**Relazione attività 1**: [Trasmissione seriale su arduino](01_TrasmissioneSerialeArduino/01_TrasmissioneSerialeArduino_Relazione.pdf).

Controllare come avviene comunicazione sulla seriale da parte di arduino.

---

# Attività 2

**Relazione attività 2**: [Comunicazione seriale con python e arduino](02_Python-2-Seriale/02_Python_2_Seriale_Relazione.pdf).

Comunicare tramite un' applicazione python che gira su Windows un sensore (potenziometro)  ed  un  attuatore  (motore  con 
L293D), entrambi realizzati su breadboard e gestiti da un programma su arduino.

Per comunicare sulla porta seriale tramite python si utilizza la libreria *serial* che può essere installata (su Windows) con il seguente comando:
```
py -m pip install pyserial
```

Documentazione ufficiale libreria [serial](https://pyserial.readthedocs.io/en/latest/pyserial.html).

---

# Attività 3

**Relazione attività 3**: [Comunicazione con pacchetto modello ISO/OSI](03_Python-3-Pacchetto_livello_3_7_del%20modello_ISO-OSI_su_seriale/03_Python_3_Pacchetto_livello_3_7_modello_ISOOSI_su_seriale_Relazione.pdf).

Come riorganizzare il formato dei messaggi scambiati fra i sensori/attuatori e l’applicazione python, preparando le cose in modo tale che possano funzionare utilizzando un RF24, che ha un payload di 32 byte.

Per realizzare questi pacchetti si utilizza la libreria *struct* già presente in python.

Documentazione ufficiale libreria [struct](https://docs.python.org/3/library/struct.html).

---

# Attività 4

**Relazione attività 4**: [Controllo sensore/attuatore tramite interfaccia grafica GUI (Python)](04_Python-4-GUI/04_Python_4_GUI_Relazione.pdf).

Come gestire il sensore e l'attuatore tramite interfaccia grafica GUI su python, 3 programmi diversi per l'attuatore e 3 per il sensore.

Per realizzare la GUI (Graphical User Interface) si utilizza la libreria *tkinter* installabile per la maggior parte degli utenti con il seguente comando:
```
py -m pip install tkinter
```

Documentazione ufficiale libreria [tkinter](https://docs.python.org/3/library/tk.html).

Nell'ultima versione del programma per il sensore, per la realizzazione del grafico si utilizza la libreria *matplotlib* installabile (su Windows) con il comando seguente:
```
py -m pip install matplotlib
```

Documentazione ufficiale libreria [matplotlib](https://matplotlib.org/).

---

# Attività 5

**Relazione attività 5**: [Memorizzazione dati sensore su un file JSON](05_Python-5-JSON/05_Python_5_JSON_Relazione.pdf).

Come memorizzare i dati ricevuti dal sensore su un file JSON in modo da poterli rendere disponibili successivamente per lo scambio di dati client/server.

Per scrivere su un file JSON da python si utilizza la libreria *json* già presente in python:

Documentazione ufficiale libreria [json](https://docs.python.org/3/library/json.html).

---

# Attività 7

**Relazione attività 7**: [Rendere disponibili sul Web i dati del sensore](07_Python-7-Flask/07_Python_7_Flask_Relazione.pdf).

Come rendere disponibili sul Web i dati del sensore memorizzati nel file JSON grazie all'utilizzo di Flask e del tunneling.

Per creare il Web server utilizzeremo la libreria *Flask* installabile (su Windows) con il comando seguente:
```
py -m pip install Flask
```

Documentazione ufficiale libreria [Flask](https://flask.palletsprojects.com/en/2.2.x/).

---

# Attività 8

**Relazione attività 8**: [Controllo del motore tramite browser](08_Python-8-Form/08_Python_8_Form_Relazione.pdf).

Come inviare dati da Web all’applicazione Flask, in modo da poter controllare il motore.

---

# Attività 9

Installazione e importazione programmi su **Raspberry**.

---

# Attività 10

**Relazione attività 10**: [Inviare pacchetti tramite modulo radio RF24](10_Pacchetto-RF24-Arduino/10_Pacchetto_RF24_Arduino_Relazione.pdf).

Come inviare i pacchetti realizzati nella fase “Pacchetto Livello 3 – seriale”, in modo che facciano uso del modulo radio **nRF24L01+**.

Per utilizzare il modulo radio **nRF24L01+** serve importare la libreria *RF24* su arduino.

Documentazione ufficiale libreria [RF24](https://nrf24.github.io/RF24/classRF24.html).
[RF24 GitHub](https://github.com/bjarne-hansen/py-nrf24).

---

# Attività 11

**Relazione attività 11**: [Controllo motore e sensore da Raspberry](11_Pacchetto-RF24-Raspberry/11_Pacchetto-RF24-Raspberry_Relazione.pdf).

Come visualizzare i dati sensore e controllare il motore tramite un server Flask che gira su **Raspberry**, che comunica con i due arduino con l'hardware tramite il modulo radio **nRF24L01+**.

Per il controllo dei piedini **GPIO** su **Raspberry** abbiamo dovuto installare la libreria *pigpiod* con il comando seguente:
```
sudo apt-get install pigpiod
```

Per interfacciarsi con il modulo radio **RF24** da python bisogna importare la libreria *nrf24* con il comando seguente:
```
python3 –m pip install nrf24  
```

---

# Attività 12

**Relazione attività 12**: [Utilizzare MQTT tra dispositivi IoT](12_Cloud-MQTT/12_Cloud_MQTT_Relazione.pdf).

Come utilizzare il protocollo MQTT per comunicare tra dispositivi IoT, anche tramite app.

Per utilizzare mqtt da python bisogna importare la libreria *paho-mqtt* con il comando seguente:
```
python3 -m pip install paho-mqtt  
```

---

# Attività 13

**Relazione attività 13**: [Utilizzare MQTT con l'ESP8266](13_Cloud-MQTT-ESP8266/13_Cloud_MQTT_ESP8266_Relazione.pdf).

Come utilizzare MQTT per lo scambio di messaggi fra dispositivi IoT connessi direttamente all'ESP8266 con funzionalità per la connessione WiFi.

Bisognerà aggiungere il gestore schede nell'IDE di Arduino per poter gestire l'ESP8266.

[Tutorial per l'installazione](https://www.vincenzov.net/tutorial/ESP/ESP8266/Arduino-IDE.htm).

---

# Attività 14

TODO: Come controllare sensore e attuatore tramite alexa.

---

# Attività 15

**Relazione attività 15**: [Utilizzare BLE per il controllo dell'ambiente](15_Cloud_BLE/15_Cloud_BLE_Relazione.pdf).

Come utilizzare ESP32 per realizzare dispositivi che utilizzano il protocollo Bluetooth Low Energy (BLE) per la comunicazione.

Per il controllo dell'ESP32 dall'IDE di Arduino bisognerà aggiungere il gestore schede come fatto precedentemente per l'ESP8266.