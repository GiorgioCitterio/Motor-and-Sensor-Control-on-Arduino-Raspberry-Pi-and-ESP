from flask import Flask
import json
import os

path = os.getcwd()+'/datiSensore.json'
app = Flask(__name__)
@app.route('/')

def returnHtml():
        with open(path, 'r') as fp:
                lista = json.load(fp)
        date = []
        valoriSensori = []
        stringa = "" 
        for i in range(len(lista)):
                date.append(lista[i]["DataOra"])
                valoriSensori.append(lista[i]["Valore"])
                stringa += "<tr><td>"+str(date[i])+"</td><td>"+str(valoriSensori[i])+"</td></tr>"
        stringaFinale= "<!DOCTYPE html><html lang=en><head><meta charset=UTF-8><meta http-equiv=X-UA-Compatible content=IE=edge><meta name=viewport content=width=device-width, initial-scale=1.0><meta http-equiv=refresh content=1><title>Dati sensore</title><style>table, th, td{border: 1px solid black;}</style></head><body><table><tr><th>Data e ora</th><th>Valore</th></tr>"+stringa+"</table></body></html>"
        print(stringaFinale)
        return stringaFinale