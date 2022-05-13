#This file will contain the paths or html can visit
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

#Defining views
#This will be our home
@views.route('/home')
def home():
    return "<h1> TEST </h1>"

@views.route('/token', methods=['GET','POST'])
def token():
    if request.method == 'POST':
        inputToken = request.form.get('editorTexto')
        print(inputToken)
        #Processing input text to tokens
        token = inputToken + 'RESULTADO ESTA A FUNCIONAR'
    return render_template("index.html", result = token)

@views.route('/grammar', methods=['GET','POST'])
def grammar():
    if request.method == 'POST':
        inputGrammar = request.form.get('editorTexto')
        print(inputGrammar)
        #Processing input text to grammar
        grammar = inputGrammar + 'RESULTADO ESTA A FUNCIONAR'
    return render_template("index.html", result = grammar)

@views.route('/about')
def about():
    return "<h1> about </h1>"