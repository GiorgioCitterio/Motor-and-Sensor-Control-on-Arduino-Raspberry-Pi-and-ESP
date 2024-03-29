import json
import plotly.express as px
import pandas as pd
import plotly
from flask import Flask, render_template
import os

path = os.getcwd()+'/datiSensore.json'
app = Flask(__name__)
@app.route('/')

def returnHtml():
   with open(path, 'r') as fp:
         lista = json.load(fp)
   date = []
   valoriSensori = []
   for i in range(len(lista)):
         date.append(lista[i]["DataOra"])
         valoriSensori.append(lista[i]["Valore"])
   df = pd.DataFrame({
   'DataOra': date,
   'Valore': valoriSensori})
   fig = px.bar(df, x='DataOra', y='Valore', barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)  
   return render_template('index.html', graphJSON=graphJSON)