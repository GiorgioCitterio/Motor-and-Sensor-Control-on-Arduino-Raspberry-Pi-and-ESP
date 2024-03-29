import tkinter as tk
import serial
import struct
import serial.tools.list_ports
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
direzione = b"A"
velocita = 0

ports = serial.tools.list_ports.comports()
comDescList = []
for port, desc, _ in sorted(ports):
    comDescList.append(port)

porta = comDescList[0]
arduino = serial.Serial(porta, 9600)
window = tk.Tk() 
window.geometry("265x100")
window.title("Controllo motore")
window.resizable(False, False)

def StampaVelocità(vel):
    velocitaText_Label = tk.Label(window, text = "Velocità = " + str(vel)).grid(row=2, column=0, pady=3)

def AumentaVelocita10():
    global velocita
    if velocita >= 250:
        velocita = 250
    else:
        velocita += 10
    StampaVelocità(velocita)
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)
    print(pack)

def DiminuisciVelocita10():
    global velocita
    if velocita <= 0:
        velocita = 0
    else:
        velocita -= 10
    StampaVelocità(velocita)
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)
    print(pack)

def DirezioneAvanti():
    global direzione
    direzione = b"A"
    StampaVelocità(velocita)
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)

def DirezioneIndietro():
    global direzione
    direzione = b"I"
    StampaVelocità(velocita)
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)

aumentaVel_button = tk.Button(text="Aumenta velocità di 10", command=AumentaVelocita10).grid(row=0, column=0, sticky="W")

dimiuisciVel_button = tk.Button(text="Dimiuisci velocità di 10", command=DiminuisciVelocita10).grid(row=0, column=1, sticky="E")

avantiDir_button = tk.Button(text="Avanti", command=DirezioneAvanti).grid(row=1, column=0, sticky="W")

indietroDir_button = tk.Button(text="Indietro", command=DirezioneIndietro).grid(row=1, column=1, sticky="E")

if __name__ == "__main__":
    window.mainloop()
    
