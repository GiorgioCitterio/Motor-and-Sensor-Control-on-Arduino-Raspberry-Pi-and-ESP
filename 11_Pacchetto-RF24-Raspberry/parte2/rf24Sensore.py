import time
import sys
import struct
import json
import pigpio
from nrf24 import *
from flask import render_template
from flask import Flask
import os

PIGPIONAME='localhost'
PIGPIOPORT=8888
READINGPIPE='00001'

IDCORRETTO='BE'
DESTINATARIOCORRETTO='P001'
MIO_TIPO='S1'

lista = []
pathJ = os.getcwd()+'/datiSensore.json'
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

@app.route('/')
def returnHtml():
    with open(pathJ, 'r') as fp:
        lista = json.load(fp)
    return render_template('index.html', dizValori=lista)
if __name__=="__main__":
    app.run(debug=True)

#lettura pacchetto 32 byte
while True:
    if nrf.data_ready():
        pack=(struct.unpack("2s 4s 4s 2s 4s 16s",nrf.get_payload()))
        id=pack[0].decode()
        mittente=pack[1].decode()
        destinatario=pack[2].decode()
        tipo=pack[3].decode()
        valoreSensore=pack[4].decode()
        vuoto=pack[5].decode()
        if ((id==IDCORRETTO)and(destinatario==DESTINATARIOCORRETTO)):
            print(pack)
            print("id e destinatario corretti e valoreSensore = " + valoreSensore)
            s=int(valoreSensore)
            dataOra = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dizionario = {'DataOra': dataOra, 'Valore' : s}
            lista.append(dizionario)
        data = json.dumps(lista[-10:])
        with open(pathJ, 'w') as fp:
                fp.write(data)
        with open(pathJ, 'r') as fp:
                lista2 = json.load(fp)
        print(lista2)