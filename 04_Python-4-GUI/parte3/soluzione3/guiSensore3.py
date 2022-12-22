import serial
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import serial.tools.list_ports
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

ports = serial.tools.list_ports.comports()
comDescList = []
for port, desc, _ in sorted(ports):
    comDescList.append(port)

porta = comDescList[0]
print(porta)
arduino = serial.Serial(porta, 9600)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
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
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(int(valoreSensore))
        xs = xs[-21:-1]
        ys = ys[-21:-1]
        ax.clear()
        ax.plot(xs, ys, marker="o")
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title("Grafico dei valori del sensore")
        plt.xlabel("X - Tempo")
        plt.ylabel("Y - Valori sensore")
    else:
        print("pacchetto scartato")

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()