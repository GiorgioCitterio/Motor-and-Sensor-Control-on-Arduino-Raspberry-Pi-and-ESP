import tkinter as tk
import serial
import time
import struct
ID=b"BE"
MITTENTE=b"M001"
DESTINATARIO=b"D031"
TIPO=b"A1"
VUOTO=b"----------------"
direzione = b"A"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("570x100")
window.title("Controllo motore")
window.resizable(False, False)

def update_lbl(val):
    if int(val)<0:
        direzione = b"I"
        vel = ~int(val)+1
        v = str(vel).zfill(3).encode()
        pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
        print(pack)
        arduino.write(pack)
    else:
        direzione = b"A"
        v = str(val).zfill(3).encode()
        pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, direzione, v, VUOTO)
        print(pack)
        arduino.write(pack)
        
velocitaText_Label = tk.Label(window, text = "Velocità:").grid(row=0, column=0, pady=4)

scale = tk.Scale(window, orient="horizontal", length=510, from_=-255.0, to=255.0, command=update_lbl, cursor="target")
scale.grid(column=1, row=0)
scale.set(0)

if __name__ == "__main__":
    window.mainloop()