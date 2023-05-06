#------------------------------------------------------------------------------- 
# programma di prova associato all'intent ProvaIntent 
#------------------------------------------------------------------------------- 
from flask import Flask, render_template 
from flask_ask import Ask, statement, question, request, session, convert_errors 
#------------------------------------------------------------------------------- 
# inizializzazione 
#------------------------------------------------------------------------------- 
app = Flask(__name__) 
ask = Ask(app, '/') 
#------------------------------------------------------------------------------- 
# funzione gestione intenti 
#------------------------------------------------------------------------------- 
@ask.launch 
def start_skill(): 
    return question("Ciao. Sono qui. Cosa vuoi fare?") 
 
@ask.intent('AMAZON.HelpIntent') 
def help(): 
    return start_skill() 
 
@ask.intent('AMAZON.FallbackIntent') 
def fallback(): 
    return statement("Si è verificato un errore") 
 
@ask.intent('AMAZON.StopIntent') 
def stop(): 
    text = "Arrivederci. Alla prossima." 
    return statement(text).simple_card('Status', text) 
 
@ask.intent('HelloWorldIntent') 
def helloWorld(): 
    return question("Ciao anche a te!") 
 
@ask.session_ended 
def session_ended(): 
    return "{}", 200 
 
@ask.intent('ProvaIntent') 
def Prova(): 
    return question('ProvaIntent sembra funzionare') 
 
#------------------------------------------------------------------------------- 
# esecuzione main 
#------------------------------------------------------------------------------- 
app.run(debug=True) 