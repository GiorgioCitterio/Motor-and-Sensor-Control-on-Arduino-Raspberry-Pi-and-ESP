import os
import shutil
import json

with open('05_Python-5-JSON/parte3/datiSensore.json', 'r') as fp:
        lista = json.load(fp)
date = []
valoriSensori = []
for i in range(len(lista)):
        date.append(lista[i]["DataOra"])
        valoriSensori.append(lista[i]["Valore"])
        stringa = "<table><tr><th>Data e ora</th><th>Valore</th></tr><tr><td>"+str(date[i])+"</td><td>"+str(valoriSensori[i])+"</td></tr></table>"
        print(stringa)