#-------------------------------------------------------------------------------
import sys
from plySimple.plySimpleLex import PlySLexObject
from plySimple.plySimpleParser import PlySimpleParser
from plySimple.plySimpleYacc import PlySYaccObject
sys.path.append('../')
from plySimple.plySimpleTokenizer import PlySimpleTokenizer

##-------------------------------------tokenizer
lexVersion = 'LEX'
yaccVersion = 'YACC'
tokenizer = PlySimpleTokenizer()
tokenizer.build()
tokenizer.lexer.begin('LEX')

##-------------------------------------parser
lex = PlySLexObject()       # lex object
yacc = PlySYaccObject()     # yacc object
parser = PlySimpleParser(lex, yacc)
lexer = parser.tokenizer.lexer
lexer.begin('LEX')
#-------------------------------------------------------------------------------



#This file will contain the paths or html can visit
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


#Defining views
#This will be our home
@views.route('/')
def home():
    return render_template("home.html")



@views.route('/token', methods=['GET','POST'])
def token():
    if request.method == 'POST':
        inputToken = request.form.get('editorTexto')
        print(inputToken)
        #Processing input text to tokens
        token = htmlTokenizer(inputToken)
        return render_template("token.html", result = token)
    return render_template("token.html")



@views.route('/grammar', methods=['GET','POST'])
def grammar():
    grammar = ""
    if request.method == 'POST':
        inputGrammar = request.form.get('editorTexto')
        print(inputGrammar)
        #Processing input text to grammar
        grammar = htmlGrammarChecker(inputGrammar)
    return render_template("grammar.html", result = grammar)



@views.route('/about')
def about():
    return render_template("about.html")




"""Recolhe input do website e devolve os tokens que foram reconhecidos"""
def htmlTokenizer(line):
    answer = ""
    tokenizer.lexer.input(line)

    tokens = [(x.type, x.value) for x in tokenizer.lexer]
    if tokens:
        for tok in tokens:
            if tok[0] == "PYTHON":
                answer = answer + "Probably python code...: " + str(tok)
            else:
                answer = answer + str(tok)
    return answer


"""Recolhe input do website e devolve a frase se reconhecida pela gramática PlySimple"""
def htmlGrammarChecker(line):
    answer = ""
    lexer.input(line)
    parseResult = parser._parser.parse(line)
    lex.reset()

    # se apenas for um pedaço de código python:
    if parseResult is not None:
        if "pythonCode" in parseResult.keys():
            if "productionRule" not in parseResult.keys():
                answer = answer + "(probably python code): " + str(parseResult)
            else:
                answer = answer + str(parseResult)
        else:
             answer = answer + str(parseResult)

    else:
        answer = answer + "#> error: could not parse... probably wrong state"
    
    return answer


