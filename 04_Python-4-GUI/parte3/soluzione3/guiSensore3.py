import tkinter as tk
import serial
import struct
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 





if __name__ == "__main__":
    window.mainloop()