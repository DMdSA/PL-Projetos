"""parser.py: Ficheiro onde estão definidas as regras de parsing da calculadora"""

import sys
sys.path.append('../')
from ply import yacc
from lexer import tokens

variablesDictionary = {}

precedence = (

    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)


def p_statement_VAR(p):
    "statement : VAR '=' exp"
    variablesDictionary[p[1]] = p[3]

def p_statement_exp(p):
    "statement : exp"
    print(p[1])

def p_exp_sum(p):
    "exp : exp '+' exp"
    p[0] = p[1] + p[3]

def p_exp_subt(p):
    "exp : exp '-' exp"
    p[0] = p[1] - p[3]

def p_exp_mult(p):
    "exp : exp '*' exp"
    p[0] = p[1] * p[3]

def p_exp_div(p):
    "exp : exp '/' exp"
    p[0] = p[1] / p[3]

def p_exp_UMINUS(p):
    "exp : '-' exp %prec UMINUS"
    p[0] = -p[2]

def p_exp_paren(p):
    "exp : '(' exp ')'"
    p[0] = p[2]

def p_exp_NUMBER(p):
    "exp : NUMBER"
    p[0] = p[1]

def p_exp_VAR(p):
    "exp : VAR"
    p[0] = getVal(p[1])

def getVal(something):
    if something not in variablesDictionary:
        print(f"Undefined name '{something}'")
    return variablesDictionary.get(something, 0)

def p_error(p):
    print(f"Syntax error at '{p.value}', [{p.lexer.lineno}]")

#def p_exp(p):
#    "expGeral : exp"
#    p[0] = p[1]
#    print(str(p[0]))
#
#def p_exp_termo(p):
#    "exp : termo"
#    p[0] = p[1]
#
#def p_exp_soma(p):
#    "exp : exp '+' termo"
#    p[0] = p[1] + [3]
#
#def p_exp_subtracao(p):
#    "exp : exp '-' termo"
#    p[0] = p[1] - p[3]
#
#def p_termo_fator(p):
#    "termo : fator"
#    p[0] = p[1]
#
#def p_termo_mult(p):
#    "termo : termo '*' fator"
#    p[0] = p[1] * p[3]
#
#def p_termo_div(p):
#    "termo : termo '/' fator"
#    p[0] = p[1] / p[3]
#
#def p_fator_NUMBER(p):
#    "fator : NUMBER"
#    p[0] = p[1]
#
#def p_fator_VAR_atrib(p):
#    "fator : VAR '=' fator"
#    p[0] = p[3]
#    print(str(p[1]) + " = " + str(p[3]))
#
#def p_fator_VAR_print(p):
#    "fator : VAR"
#    p[0]
#
#def p_fator_exp(p):
#    "fator : '(' exp ')'"
#    p[0] = p[2]
#
#



parser = yacc.yacc()
res = 0

for line in sys.stdin:
    parser.parse(line)