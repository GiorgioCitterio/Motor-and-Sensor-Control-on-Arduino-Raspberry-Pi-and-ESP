import paho.mqtt.client as client
from flask import Flask, request, render_template, redirect
import struct
import json
import time
import sys
import pigpio
from nrf24 import *

#costanti rf24
PIGPIONAME='localhost'
PIGPIOPORT=8888
WRITINGPIPE='00001'

#costanti motore
ID=b"BE"
MITTENTE=b"P001"
DESTINATARIO=b"A001"
TIPO=b"A1"
VUOTO=("-"*16).encode()

#costanti mqtt
TOPIC="tps/motoreAtt"
BROKER = "172.17.4.29"

lista = []
direzione = b"A"
app = Flask(__name__)

def on_connect(subscriber, userdata, flags, rc):
    print("Connesso con return code" + str(rc))

    subscriber.subscribe(TOPIC)

def on_message(subscriber, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

subscriber = client.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

subscriber.connect(BROKER, 1883, 60)

subscriber.loop_forever()

# connessione a pigpiod 
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT) 
if not pi.connected: 
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD") 
    sys.exit() 
 
# Crea l'oggetto NRF24  
nrf = NRF24(pi, ce=17, payload_size=32, channel=76,data_rate=RF24_DATA_RATE.RATE_2MBPS, pa_level=RF24_PA.LOW) 
 
# apre le pipe 
nrf.set_address_bytes(5) 
nrf.open_writing_pipe(WRITINGPIPE)

#programma sensore
@app.route('/')
def returnHtml():
    with open(pathJ, 'r') as fp:
        lista = json.load(fp)
    return render_template('index.html', dizValori=lista)
if __name__=="__main__":
    app.run(debug=True)

#programma attuatore
@app.route("/ricevi")
def riceviForm():
    val = request.args["velocita"]
    if(request.args["btn"] == "avanti"):
        direzione = b"A"
    else:
        direzione = b"I"
    v = str(val).zfill(3).encode()
    msg=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO,TIPO,direzione,v,VUOTO)
    nrf.send(msg)
    print(msg)
    nrf.wait_until_sent() #funzione per la sincronizzazione del modulo rf24 dopo l'invio
    nrf.power_up_rx() #funzione che rimette il modulo in ascolto
    return redirect("/")