import time
import sys
import pigpio
from nrf24 import *
import struct
from flask import Flask, request, render_template

PIGPIONAME='localhost'
PIGPIOPORT=8888
WRITINGPIPE='00001'
ID=b"BE"
MITTENTE=b"P001"
DESTINATARIO=b"A001"
TIPO=b"A1"
VUOTO=("-"*16).encode()
direzione = b"A"
app = Flask(__name__)

# connessione a pigpiod
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT)
if not pi.connected:
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD")
    sys.exit()

# Crea l'oggetto NRF24
nrf = NRF24(pi, ce=17, payload_size=32, channel=76,data_rate=RF24_DATA_RATE.RATE_1MBPS, pa_level=RF24_PA.LOW)

# apre le pipe
nrf.set_address_bytes(5)
nrf.open_writing_pipe(WRITINGPIPE)

#scrittura pacchetto 32 byte
@app.route("/")
def inviaFormVuoto():
    return(render_template("index.html"))

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
    return("Velocità: "+request.args["velocita"] + " " + "Direzione: " + request.args["btn"])
