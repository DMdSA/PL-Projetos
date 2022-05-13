#This file will contain the paths or html can visit
from flask import Blueprint, render_template, request

#-------------------------------------------------------------------------------
import sys
sys.path.append('../')
from plySimple.plySimpleTokenizer import PlySimpleTokenizer

lexVersion = 'LEX'
yaccVersion = 'YACC'
tokenizer = PlySimpleTokenizer()
tokenizer.build()
tokenizer.lexer.begin('LEX')
#-------------------------------------------------------------------------------


views = Blueprint('views', __name__)

#Defining views
#This will be our home
@views.route('/home')
def home():
    return "<h1> TEST </h1>"

@views.route('/token', methods=['GET','POST'])
def token():
    token = ""
    if request.method == 'POST':
        inputToken = request.form.get('editorTexto')
        print(inputToken)
        #Processing input text to tokens
        token = htmlTokenizer(inputToken)
        
    return render_template("index.html", result = token)

@views.route('/grammar', methods=['GET','POST'])
def grammar():
    grammar = ""
    if request.method == 'POST':
        inputGrammar = request.form.get('editorTexto')
        print(inputGrammar)
        #Processing input text to grammar
        grammar = inputGrammar + 'RESULTADO ESTA A FUNCIONAR'
    return render_template("index.html", result = grammar)

@views.route('/about')
def about():
    return "<h1> about </h1>"




def htmlTokenizer(line):
    answer = ""
    tokenizer.lexer.input(line)

    tokens = [(x.type, x.value) for x in tokenizer.lexer]
    if tokens:
        for tok in tokens:
            if tok[0] == "PYTHON":
                answer = answer + "<br>Probably python code...: " + str(tok)
            else:
                answer = answer + str(tok)
    return answer