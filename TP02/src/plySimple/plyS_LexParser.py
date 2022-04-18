"""plySParser.py: Definição do parser para a linguagem PLYSIMPLE"""

import sys
sys.path.append('../')
from ply import yacc

from plyS_LexTokenizer import lexer, tokens
from plySimpleLex import plySLex, error_key, return_key, regex_key, comment_key, lineno_key

lexObject = plySLex()

start = "start"
## START OPTIONS

def p_start_init(p):
    "start : init"
    p[0] = p[1]

def p_start_regexRules(p):
    "start : regexRules"
    p[0] = p[1]

def p_start_comment(p):
    "start : comment"
    p[0] = p[1]
    comment = {comment_key : p[0]}
    #adicionar!

def p_start_fim(p):
    "start : "


## INITIALIZE PLY - LEXER

def p_init_LITERALS(p):
    "init : '%' LITERALS '=' CHARS comment"
    lit = {p[2] : p[4], lineno_key : lexer.lineno, comment_key : p[5]}
    lexObject.addVariable(lit)
    #lexObject.printVariables()

def p_init_IGNORE(p):
    "init : '%' IGN '=' CHARS comment"
    ign = {p[2] : p[4], lineno_key : lexer.lineno, comment_key : p[5]}
    lexObject.addVariable(ign)
    #lexObject.printVariables()                      # cuidado com os \\n !
    #print("\n" + str(plyDictionary))

def p_init_tokens(p):
    "init : '%' TKNS '=' '[' vars ']' comment"
    tks = {p[2] : p[5], lineno_key : lexer.lineno, comment_key : p[7]}
    lexObject.addVariable(tks)
    #lexObject.printVariables()

def p_init_fim(p):
    "init : "

def p_vars_variaveis(p):
    "vars : vars ',' VAR"
    p[0] = p[1] + [p[3]]

def p_vars_var(p):
    "vars : VAR"
    p[0] = [p[1]]


## REGEX RULES - LEXER

def p_regexRules_regex_regex(p):
    "regexRules : REGEX RETURN '(' regexReturn ')' comment"
   # print("regex01: " + p[1] + ", " + "return: " + str(p[4]))

    variavel = (p[4])[0]
    if lexObject.checkTokenExistance(variavel) is False:
        raise Exception("Symbol '{variavel}' used, but not defined as a rule or a token!")
    
    tipo = (p[4])[1]
    ret = {return_key : variavel, variavel : tipo, regex_key : p[1], lineno_key : lexer.lineno, comment_key : p[6]}
    lexObject.addVariable(ret)
    #lexObject.printVariables()


def p_regexRules_regex_var(p):
    "regexRules : VAR RETURN '(' regexReturn ')' comment"
    #print("regex02: " + p[1] + ", " + "return: " + str(p[4]))
    
    variavel = (p[4])[0]
    if lexObject.checkTokenExistance(variavel) is False:
        raise Exception("Symbol '{variavel}' used, but not defined as a rule or a token!")
    tipo = (p[4])[1]
    
    ret = {return_key : variavel, variavel : tipo, regex_key : p[1], lineno_key : lexer.lineno, comment_key : p[6]}
    lexObject.addVariable(ret)
    #lexObject.printVariables()
    

def p_regexRules_error(p):
    "regexRules : errorRules comment"
    p[0] = p[1]
    err = {error_key : p[0], lineno_key : lexer.lineno, comment_key : p[2]}
    lexObject.addVariable(err)


def p_regexReturn_var(p):
    "regexReturn : VAR"
    p[0] = (p[1], "str")

def p_regexReturn_varresult(p):
    "regexReturn : VAR ',' PLYTVALUE"
    p[0] = (p[1], p[3])

def p_regexReturn_vartype(p):
    "regexReturn : VAR ',' RETTYPE '(' PLYTVALUE ')'"
    p[0] = (p[1], p[3])


def p_errorRules(p):
    "errorRules : REGEX ERROR '(' errorValues ')'"
    p[0] = p[4]


def p_errorValuesFSTR(p):
    "errorValues : FSTR"
    p[0] = p[1]
    # o resultado é apenas uma string formatada

def p_errorValuesSkip(p):
    "errorValues : TSKIP"
    p[0] = p[1]

def p_errorValuesMoreV1(p):
    "errorValues : FSTR ',' TSKIP"
    p[0] = (p[1], p[3])

def p_errorValuesMoreV2(p):
    "errorValues : TSKIP ',' FSTR"
    p[0] = (p[3], p[1])

## COMMENTS

def p_comment(p):
    "comment : COMMENT"
    p[0] = p[1]


def p_comment_fim(p):
    "comment : "
    p[0] = ""

def p_error(p):
        print(f"Syntax error at '{p.value}', {p}")



lexParser = yacc.yacc()

fHandler = open("lexteste.txt", "rt", encoding="utf-8")
for line in fHandler:
    lexParser.parse(line)

fHandler.close()
lexObject.printVariables()
if lexObject.isReady:
    print("\n#> ESTÁ PRONTO O LEXER!")