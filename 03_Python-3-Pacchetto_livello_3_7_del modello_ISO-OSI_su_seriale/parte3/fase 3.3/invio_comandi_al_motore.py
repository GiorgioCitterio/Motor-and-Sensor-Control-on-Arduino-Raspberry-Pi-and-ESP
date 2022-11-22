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
    d = input("direzione ")
    DIREZIONE = str(d).zfill(3).encode()
    v = int(input("velocita "))
    VELOCITA=str(v).zfill(1).encode()
    pack=struct.pack("2s 4s 4s 2s 3s 1s 16s",ID,MITTENTE,DESTINATARIO, DIREZIONE, VELOCITA, TIPO, VUOTO)
    arduino.write(pack)
    print(pack)