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
    pack=struct.pack("2s 4s 4s 2s 16s",ID,MITTENTE,DESTINATARIO, TIPO, VUOTO)