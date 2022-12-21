# tps_2022_2023
tps_GiorgioCitterio_UmbertoColombo_2022_2023       

---

# Attività 1

**Relazione attività 1**: [Trasmissione seriale su arduino](01_TrasmissioneSerialeArduino/01_TrasmissioneSerialeArduino_Relazione.pdf).

Controllare come avviene comunicazione sulla seriale da parte di arduino.

---

# Attività 2

**Relazione attività 2**: [Comunicazione seriale con python e arduino](02_Python-2-Seriale/02_Python_2_Seriale_Relazione.pdf).

Comunicare tramite un' applicazione python che gira su Windows un sensore (potenziometro)  ed  un  attuatore  (motore  con 
L293D), entrambi realizzati su breadboard e gestiti da un programma su arduino.

Per comunicare sulla porta seriale tramite python si utilizza la libreria *serial* che può essere installata (su Windows) con il seguente comando:
`py -m pip install pyserial`

Documentazione ufficiale libreria [serial](https://pyserial.readthedocs.io/en/latest/pyserial.html).

---

# Attività 3

**Relazione attività 3**: [Comunicazione con pacchetto modello ISO/OSI](03_Python-3-Pacchetto_livello_3_7_del%20modello_ISO-OSI_su_seriale/03_Python_3_Pacchetto_livello_3_7_modello_ISOOSI_su_seriale_Relazione.pdf).

Come riorganizzare il formato dei messaggi scambiati fra i sensori/attuatori e l’applicazione python, preparando le cose in modo tale che possano funzionare utilizzando un RF24, che ha un payload di 32 byte.

Per realizzare questi pacchetti si utilizza la libreria *struct* già presente in python.

Documentazione ufficiale libreria [struct](https://docs.python.org/3/library/struct.html)

---

# Attività 4

**Relazione attività 4**: [Controllo sensore/attuatore tramite interfaccia grafica GUI (Python)](04_Python-4-GUI/04_Python_4_GUI_Relazione.pdf).

Come gestire il sensore e l'attuatore tramite interfaccia grafica GUI su python, 3 programmi diversi per l'attuatore e 3 per il sensore.

Per realizzare la GUI (Graphical User Interface) si utilizza la libreria *tkinter* già presente in python:

Documentazione ufficiale libreria [tkinter](https://docs.python.org/3/library/tk.html).

Nell'ultima versione del programma per il sensore, per la realizzazione del grafico si utilizza la libreria *matplotlib* installabile (su Windows) con il comando seguente:
`py -m pip install matplotlib`

Documentazione ufficiale libreria [matplotlib](https://matplotlib.org/).

---

# Attività 5

**Relazione attività 5**: [Memorizzazione dati sensore su un file JSON](05_Python-5-JSON/05_Python_5_JSON_Relazione.pdf).

Come memorizzare i dati ricevuti dal sensore su un file JSON in modo da poterli rendere disponibili successivamente per lo scambio di dati client/server.

Per scrivere su un file JSON da python si utilizza la libreria *json* già presente in python:

Documentazione ufficiale libreria [json](https://docs.python.org/3/library/json.html).
