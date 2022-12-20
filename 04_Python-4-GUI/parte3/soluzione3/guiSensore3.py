import serial
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
graf = plt.figure()
ax = graf.add_subplot(1, 1, 1)

def GrafFunz(i, x, y):
    x.append(i)
    y.append(int(valoreSensore))
    ax.clear()
    ax.plot(x, y)
    ax.title("Il grafico dei valori del sensore")
    ax.xlabel("X - Secondi")
    ax.ylabel("Y - Valori sensore")
    ax.axes([0, i, 0, 1023])

for i in range(20):
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
        ani = animation.FuncAnimation(graf, GrafFunz,fargs=(i, valoreSensore), interval=1000)
        plt.show()
    else:
        print("pacchetto scartato")