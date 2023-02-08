from flask import Flask, request, render_template
import serial
import struct
import os
import json
import time
import serial.tools.list_ports
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"
direzione = b"A"

pathJ = os.getcwd()+'/datiSensore.json'
pathH = os.getcwd()+'/templates/index.html'
ports = serial.tools.list_ports.comports()
porteSeriali = []
for port, desc, _ in sorted(ports):
    porteSeriali.append(port)
arduinoSensore = serial.Serial(porteSeriali[0], 9600)
arduinoAttuatore = serial.Serial(porteSeriali[1], 9600)
app = Flask(__name__)
lista = []

while True:
    val = arduinoSensore.read(32)
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
    with open(pathJ, 'w') as fp:
        fp.write(data)
    with open(pathJ, 'r') as fp:
        lista2 = json.load(fp)

    @app.route("/ricevi2")
    def returnHtml():
        with open(pathJ, 'r') as fp:
            lista = json.load(fp)
        return(render_template('index.html', dizValori=lista))
        
    @app.route("/ricevi2")
    def riceviForm():
        val = request.args["velocita"]
        if(request.args["btn"] == "avanti"):
            direzione = b"A"
        else:
            direzione = b"I"
        v = str(val).zfill(3).encode()
        pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
        print(pack)
        arduinoAttuatore.write(pack)
        return("Velocità: "+request.args["velocita"] + " " + "Direzione: " + request.args["btn"])