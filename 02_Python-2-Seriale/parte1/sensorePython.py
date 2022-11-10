import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(1)

print('inizio ricezione dei dati')
while True:
    b = bytearray(arduino.readline())
    s = int(b.decode())
    print(s)
    time.sleep(0.5)