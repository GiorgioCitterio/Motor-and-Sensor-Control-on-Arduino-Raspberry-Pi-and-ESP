import serial
import struct
import json
import time
import serial.tools.list_ports
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

ports = serial.tools.list_ports.comports()
portaSeriale = []
for port, desc, _ in sorted(ports):
    portaSeriale.append(port)

arduino = serial.Serial(portaSeriale[0], 9600)
lista = []

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
    else:
        print("pacchetto scartato")
    data = json.dumps(lista[-10:])  
    with open('05_Python-5-JSON/parte3/datiSensore.json', 'w') as fp:
        fp.write(data)
    with open('05_Python-5-JSON/parte3/datiSensore.json', 'r') as fp:
        lista2 = json.load(fp)
    with open('07_Python-7-Flask/parte3/datiSensore.json', 'w') as fp:
        fp.write(data)
    with open('07_Python-7-Flask/parte3/datiSensore.json', 'r') as fp:
        lista2 = json.load(fp)
    print(lista2)