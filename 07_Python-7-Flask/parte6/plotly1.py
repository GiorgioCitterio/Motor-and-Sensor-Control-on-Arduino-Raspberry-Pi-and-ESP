import json
import dash
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os

app = Flask(__name__)
@app.route('/')

def funz():
   app = dash.Dash(__name__)
   path = os.getcwd()+'/datiSensore.json'
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
   app.layout = html.Div(children=[
      html.H1(children='Valori sensore'),
      html.Div(children='''
      Ploty: Estratto file JSON.
      '''),
      dcc.Graph(
         id='example-graph',
         figure=fig
      )
   ]) 
   return "a"
