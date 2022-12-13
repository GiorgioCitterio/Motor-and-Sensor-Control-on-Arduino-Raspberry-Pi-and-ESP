import tkinter as tk
import serial
import struct
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
C = tk.Canvas(window, bg="purple", height=250, width=300)
C.pack()

rettangolo = C.create_rectangle(0, 0, 0, 0)

def funz(window):
    global rettangolo     
    C.delete(rettangolo)
    val = arduino.read(32)
    pack = struct.unpack("2s 4s 4s 2s 4s 16s", val)
    print(pack)
    id=pack[0].decode()
    mittente=pack[1].decode()
    destinatario=pack[2].decode()
    tipo=pack[3].decode()
    valoreSensore=pack[4].decode()
    vuoto=pack[5].decode()
    if (id==IDCORRETTO)and(destinatario==DESTINATARIOCORRETTO):
        print("id e destinatario corretti, valore del sensore = "+valoreSensore)
        v = int(valoreSensore)
        coordinate = 30, 90, v/4, 200
        rettangolo = C.create_rectangle(coordinate, fill="yellow")
    else:
        print("pacchetto scartato")    

    window.after(1000, funz, window)
    
window.after(1000, funz, window) 

if __name__ == "__main__":
    window.mainloop()