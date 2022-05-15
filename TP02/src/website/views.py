#-------------------------------------------------------------------------------
import sys
sys.path.append('../')
import re
from plySimple.plySimpleLex import PlySLexObject
from plySimple.plySimpleParser import PlySimpleParser
from plySimple.plySimpleYacc import PlySYaccObject
from plySimple.plySimpleTokenizer import PlySimpleTokenizer

##-------------------------------------tokenizer
lexVersion = 'LEX'
yaccVersion = 'YACC'
tokenizer = PlySimpleTokenizer()
tokenizer.build()
tokenizer.lexer.begin('LEX')


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
        return render_template("token.html", result = token, original = inputToken)
    return render_template("token.html")



@views.route('/grammar', methods=['GET','POST'])
def grammar(): 
    if request.method == 'POST':
        inputGrammar = request.form.get('editorTexto')
        print(inputGrammar)
        #Processing input text to grammar
        grammar = htmlGrammarChecker(inputGrammar)
        return render_template("grammar.html", result = grammar, original = inputGrammar)
    return render_template("grammar.html")


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
                answer = answer + "Probably python code...: " + str(tok) + "\n"
            else:
                answer = answer + str(tok) + "\n"
    return answer


"""Recolhe input do website e devolve a frase se reconhecida pela gramática PlySimple"""
#def htmlGrammarChecker(text):
#
#    answer = ""
#    eachLine = re.findall(r'.+\n?', text)
#    eachLine = [re.sub(r'\r?\n', "", x) for x in eachLine]
#    print(eachLine)
#
#    auxString = ""
#
#    for l in eachLine:
#
#        if l:
#            lexer.input(l)
#            [x.value for x in lexer]
#            auxString = auxString + l
#
#            if parser.tokenizer.insideMultiline() is False:
#                parseResult = parser._parser.parse(auxString)
#                print(str(type(parseResult)) + " " + str(parseResult))
#                # se apenas for um pedaço de código python:
#                if parseResult is not None:
#                    if "pythonCode" in parseResult.keys():
#                        if "productionRule" not in parseResult.keys():
#                            answer = answer + "(probably python code): " + str(parseResult) + "\n"
#                        else:
#                            answer = answer + str(parseResult) + "\n"
#                    else:
#                         answer = answer + str(parseResult) + "\n"
#                else:
#                    answer = answer + "#> error: could not parse... probably wrong state\n"
#                auxString = ""
#
#
#    lex.reset()
#    return answer
#

"""Recolhe input do website e devolve a frase se reconhecida pela gramática PlySimple"""
def htmlGrammarChecker(text):

    ##-------------------------------------parser
    lex = PlySLexObject()       # lex object
    yacc = PlySYaccObject()     # yacc object
    parser = PlySimpleParser(lex, yacc)
    lexer = parser.tokenizer.lexer
    lexer.begin('LEX')

    answer = ""
    auxString = ""
    #dividir texto em linhas
    list_of_lines = text.splitlines(keepends=True)

    for line in list_of_lines:
        if line: 
              
            if not re.match(r'^\s*$', line):
                lexer.input(line)
                [x.value for x in lexer]
                auxString = auxString + line  

                if parser.tokenizer.insideMultiline() is False:
                    parseResult = parser._parser.parse(auxString)
                    # se apenas for um pedaço de código python:
                    if parseResult is not None:
                        if "pythonCode" in parseResult.keys():
                            if "productionRule" not in parseResult.keys():
                                answer = answer + "(probably python code): " + str(parseResult) + "\n"
                            else:
                                answer = answer + str(parseResult) +"\n"
  
                        else:
                            answer = answer + str(parseResult) + "\n"

                    else:
                        answer = answer + "#> error: could not parse... probably wrong state \n"
                    auxString = ""
    return answer
