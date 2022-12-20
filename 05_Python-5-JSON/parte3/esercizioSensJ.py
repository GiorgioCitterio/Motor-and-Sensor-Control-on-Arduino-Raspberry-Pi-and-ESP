import serial
import struct
import json
import time
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)

lista = []
cont = 0

while True:
    val = arduino.read(32)
    pack = struct.unpack("2s 4s 4s 2s 4s 16s", val)
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
        cont += 1
    else:
        print("pacchetto scartato")

    if cont>10:
        data = json.dumps(lista[-10:])
        with open('05_Python-5-JSON/parte3/datiSensore.json', 'w') as fp:
            fp.write(data)
        with open('05_Python-5-JSON/parte3/datiSensore.json', 'r') as fp:
            lista2 = json.load(fp)
        print(lista2)
        #time.sleep(30)