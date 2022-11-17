import serial;
import time;
import struct;

arduino = serial.Serial('COM3', 9600)

print('inizio invio dei dati')
while True:
    val = arduino.read(32)
    print(val)