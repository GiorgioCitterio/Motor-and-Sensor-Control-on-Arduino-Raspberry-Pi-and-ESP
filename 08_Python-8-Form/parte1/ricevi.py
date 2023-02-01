from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def inviaFormVuoto():
    return(render_template("index.html"))

@app.route("/ricevi")
def riceviForm():
    print(request.args["velocita"])
    return(request.args["velocita"])