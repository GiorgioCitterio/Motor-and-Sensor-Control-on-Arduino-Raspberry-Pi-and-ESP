import tkinter as tk
import serial
import struct
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
direzione = b"A"
velocita = 0

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("265x100")
window.title("Controllo motore")
window.resizable(False, False)

def DirezioneAvanti():
    global direzione
    direzione = b"A"
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)

def DirezioneIndietro():
    global direzione
    direzione = b"I"
    v=str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    arduino.write(pack)

avantiDir_button = tk.Button(text="Avanti", command=DirezioneAvanti)
avantiDir_button.grid(row=1, column=0, sticky="W")

indietroDir_button = tk.Button(text="Indietro", command=DirezioneIndietro)
indietroDir_button.grid(row=1, column=1, sticky="E")

if __name__ == "__main__":
    window.mainloop()