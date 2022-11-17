import serial;
import time;
import struct;
IDCORRETTO = "BE"

arduino = serial.Serial('COM3', 9600)

print('inizio invio dei dati')
while True:
    val = arduino.read(32)
    pack = struct.unpack("2s 4s 4s 2s 4s 16s", val)
    id=pack[0].decode()
    mittente=pack[1]
    destinatario=pack[2]
    tipo=pack[3]
    valoreSensore=pack[4]
    vuoto=pack[5]
    if id==IDCORRETTO:
        print("id corretto")
    else:
        print("pacchetto scartato")
    