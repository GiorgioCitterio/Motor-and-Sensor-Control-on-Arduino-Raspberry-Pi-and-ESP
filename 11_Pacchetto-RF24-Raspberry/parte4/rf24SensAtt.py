from flask import Flask, request, render_template
import struct
import os
import json
import time
import sys
import pigpio
from nrf24 import *

#costanti rf24
PIGPIONAME='localhost'
PIGPIOPORT=8888
READINGPIPE='00001'

#costanti motore
ID=b"BE"
MITTENTE=b"P001"
DESTINATARIO=b"A001"
TIPO=b"A1"
VUOTO=("-"*16).encode()

lista = []
pathJ = os.getcwd()+'/datiSensore.json'
direzione = b"A"
app = Flask(__name__)

# connessione a pigpiod
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT)
if not pi.connected:
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD")
    sys.exit()

# Crea l'oggetto NRF24
nrf = NRF24(pi, ce=17, payload_size=32, channel=76,data_rate=RF24_DATA_RATE.RATE_2MBPS, pa_level=RF24_PA.LOW)

# apre la pipe
nrf.set_address_bytes(5)
nrf.open_reading_pipe(RF24_RX_ADDR.P1, READINGPIPE)

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
    nrf.wait_until_sent()
    nrf.power_up_rx()
    return("Velocità: "+request.args["velocita"] + " " + "Direzione: " + request.args["btn"])