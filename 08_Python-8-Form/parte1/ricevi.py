from flask import Flask, request, render_template
import serial
import struct
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
direzione = b"A"

arduino = serial.Serial('COM3', 9600)
app = Flask(__name__)

@app.route("/")
def inviaFormVuoto():
    return(render_template("index.html"))

@app.route("/ricevi")
def riceviForm():
    val = request.args["velocita"]
    if(request.args["btn"] == "avanti"):
        direzione = b"A"
        v = str(val).zfill(3).encode()
    else:
        direzione = b"I"
        vel = ~int(val)+1
        v = str(vel).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    print(pack)
    arduino.write(pack)
    return(request.args["velocita"] + " " + request.args["btn"])