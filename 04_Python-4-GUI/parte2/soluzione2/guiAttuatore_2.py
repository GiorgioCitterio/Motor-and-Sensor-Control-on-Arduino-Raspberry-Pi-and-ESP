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
window.geometry("225x60")
window.title("Controllo motore")
window.resizable(False, False)

def DirezioneAvanti():
    global direzione
    global velocita
    direzione = b"A"
    velocita = entry1.get()
    if int(velocita) > 255:
        velocita = 255
        entry1.delete(0, tk.END)
        entry1.insert(0, "255")
    elif int(velocita) < 0:
        velocita = 0
        entry1.delete(0, tk.END)
        entry1.insert(0, "0")
    v = str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    print(pack)
    arduino.write(pack)

def DirezioneIndietro():
    global direzione
    global velocita
    direzione = b"I"
    velocita = entry1.get()
    if int(velocita)>255:
        velocita = 255
        entry1.delete(0, tk.END)
        entry1.insert(0, "255")
    elif int(velocita) < 0:
        velocita = 0
        entry1.delete(0, tk.END)
        entry1.insert(0, "0")
    v = str(velocita).zfill(3).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
    print(pack)
    arduino.write(pack)

avantiDir_button = tk.Button(text="Avanti", command=DirezioneAvanti).grid(row=0, column=0)

indietroDir_button = tk.Button(text="Indietro", command=DirezioneIndietro).grid(row=0, column=2)

velocitaText_Label = tk.Label(window, text = "Velocità:").grid(row=1, column=0, pady=5)

entry1 = tk.Entry(window, width=20)
entry1.grid(row=1, column=1)

if __name__ == "__main__":
    window.mainloop()