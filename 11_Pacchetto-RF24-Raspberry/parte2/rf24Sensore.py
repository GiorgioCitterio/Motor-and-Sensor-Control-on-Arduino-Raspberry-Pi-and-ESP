import time
import sys
import struct
import json
import pigpio
from nrf24 import *

PIGPIONAME='localhost'
PIGPIOPORT=8888
READINGPIPE='00001'

IDCORRETTO=b"BE"
DESTINATARIOCORRETTO=b"P001"
MIO_TIPO=b"S1"

lista = []

# connessione a pigpiod
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT)
if not pi.connected:
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD")
    sys.exit()

# Crea l'oggetto NRF24
nrf = NRF24(pi, ce=17, payload_size=32, channel=76,
data_rate=RF24_DATA_RATE.RATE_1MBPS, pa_level=RF24_PA.LOW)

# apre la pipe
nrf.set_address_bytes(5)
nrf.open_reading_pipe(RF24_RX_ADDR.P1, READINGPIPE)

#lettura pacchetto 32 byte
while True:
    if nrf.data_ready():
        pack=(struct.unpack("2s 4s 4s 2s 4s 16s",nrf.get_payload()))
        print(pack)
        id=pack[0].decode()
        mittente=pack[1].decode()
        destinatario=pack[2].decode()
        tipo=pack[3].decode()
        valoreSensore=pack[4].decode()
        vuoto=pack[5].decode()
        if (id==IDCORRETTO)and(destinatario==DESTINATARIOCORRETTO):
            print("id e destinatario corretti e valoreSensore = " + valoreSensore)
            s=int(valoreSensore)
            dataOra = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dizionario = {'DataOra': dataOra, 'Valore' : s}
            lista.append(dizionario)
        else:
            print("pacchetto scartato")
        data = json.dumps(lista[-10:])
        with open('11_Pacchetto-RF24-Raspberry/datiSensore.json', 'w') as fp:
                fp.write(data)
        with open('11_Pacchetto-RF24-Raspberry/datiSensore.json', 'r') as fp:
                lista2 = json.load(fp)
        print(lista2)