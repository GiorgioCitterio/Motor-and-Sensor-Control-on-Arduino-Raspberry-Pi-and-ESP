from flask import Flask, request, render_template
import serial
import struct
import os
import json
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"
direzione = b"A"

pathJ = os.getcwd()+'/datiSensore.json'

arduinoAttuatore = serial.Serial('COM3', 9600)
app = Flask(__name__)

lista = []
@app.route('/')

def returnHtml():
        with open(pathJ, 'r') as fp:
                lista = json.load(fp)
        return render_template('index.html', dizValori=lista)

@app.route("/ricevi")
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