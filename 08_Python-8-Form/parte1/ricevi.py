from flask import Flask, request, render_template
import serial
import struct
import serial.tools.list_ports
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
direzione = b"A"

ports = serial.tools.list_ports.comports()
comDescList = []
for port, desc, _ in sorted(ports):
    comDescList.append(port)

arduino = serial.Serial(comDescList[0], 9600)
app = Flask(__name__)

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
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    print(pack)
    arduino.write(pack)
    return("Velocità: "+request.args["velocita"] + " " + "Direzione: " + request.args["btn"])