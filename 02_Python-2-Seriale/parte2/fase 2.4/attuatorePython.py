import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(1)

print('inizio invio dei dati')
while True:
    val = input("direzione;velocità"+"\n")
    arduino.write(val)
    print(val)
