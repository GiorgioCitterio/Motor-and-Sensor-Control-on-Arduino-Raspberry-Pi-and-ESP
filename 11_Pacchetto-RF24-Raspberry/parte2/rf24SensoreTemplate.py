from flask import render_template
from flask import Flask
import os
import json

pathJ = os.getcwd()+'/datiSensore.json'
app = Flask(__name__)
@app.route('/')

def returnHtml():
    with open(pathJ, 'r') as fp:
        lista = json.load(fp)
    return render_template('index.html', dizValori=lista)
if __name__=="__main__":
    app.run(debug=True)