import serial;
import struct;
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"

arduino = serial.Serial('COM3', 9600)

print('inizio invio dei dati')
while True:
    d = input("direzione a/i: ")
    DIREZIONE = str(d).zfill(1).encode()
    v = input("velocità: ")
    VELOCITA=str(v).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, DIREZIONE, VELOCITA, VUOTO)
    arduino.write(pack)
    print(pack)
