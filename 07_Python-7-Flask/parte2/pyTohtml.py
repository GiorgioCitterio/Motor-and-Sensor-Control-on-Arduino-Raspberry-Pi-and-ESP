import os
import shutil
import json

with open('05_Python-5-JSON/parte3/datiSensore.json', 'r') as fp:
        lista = json.load(fp)
date = []
valoriSensori = []
stringa = "" 
for i in range(len(lista)):
        date.append(lista[i]["DataOra"])
        valoriSensori.append(lista[i]["Valore"])
        stringa += "<tr><td>"+str(date[i])+"</td><td>"+str(valoriSensori[i])+"</td></tr>"
stringaFinale= "<style>table, th, td{border: 1px solid black;}</style><body><table><tr><th>Data e ora</th><th>Valore</th></tr>"+stringa+"</table></body>"
print (stringaFinale)
with open("07_Python-7-Flask/parte2/index.html", "w") as ft:
        ft.write(stringaFinale)