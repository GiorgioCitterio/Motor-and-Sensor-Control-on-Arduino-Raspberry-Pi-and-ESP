import serial
import struct
import json
import time
import serial.tools.list_ports
import os
from flask import Flask
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
    print(lista2)
    path = os.getcwd()+'/datiSensore.json'
    app = Flask(__name__)
    @app.route('/')
    def returnHtml():
        with open(path, 'r') as fp:
                lista = json.load(fp)
        date = []
        valoriSensori = []
        stringa = "" 
        for i in range(len(lista)):
                date.append(lista[i]["DataOra"])
                valoriSensori.append(lista[i]["Valore"])
                stringa += "<tr><td>"+str(date[i])+"</td><td>"+str(valoriSensori[i])+"</td></tr>"
        stringaFinale= "<style>table, th, td{border: 1px solid black;}</style><body><table><tr><th>Data e ora</th><th>Valore</th></tr>"+stringa+"</table></body>"
        print(stringaFinale)
        return stringaFinale
    if os.path.exists("05_Python-5-JSON/parte3/datiSensore.json"):
        os.remove("05_Python-5-JSON/parte3/datiSensore.json")
        print("file rimosso")
    else:
        print("The file does not exist")
