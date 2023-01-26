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


@app.route('/')
def returnHtml():
    return(render_template('index.html'))


@app.route("/ricevi")
def riceviForm():
    return(request.args["Velocità"])