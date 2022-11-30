import tkinter as tk
import serial
import struct
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("265x100")
window.title("Controllo motore")
window.resizable(False, False)

def AumentaVelocita10():
    text = "Hello World!"

def DiminuisciVelocita10():
    text = "Nuovo Messaggio! Nuova Funzione!"

def DirezioneAvanti():
    DIREZIONE  = "A"

def DirezioneIndietro():
    DIREZIONE = "I"

aumentaVel_button = tk.Button(text="Aumenta velocità di 10", command=AumentaVelocita10)
aumentaVel_button.grid(row=0, column=0, sticky="W")

dimiuisciVel_button = tk.Button(text="Dimiuisci velocità di 10", command=DiminuisciVelocita10)
dimiuisciVel_button.grid(row=0, column=1, sticky="E")

avantiDir_button = tk.Button(text="Avanti", command=DirezioneAvanti)
avantiDir_button.grid(row=1, column=0, sticky="W")

indietroDir_button = tk.Button(text="Indietro", command=DirezioneIndietro)
indietroDir_button.grid(row=1, column=1, sticky="E")

while True:
    window.mainloop()
    DIREZIONE = "A"
    VELOCITA = 135
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, DIREZIONE, VELOCITA, VUOTO)
    arduino.write(pack)
#if __name__ == "__main__":
#   window.mainloop()