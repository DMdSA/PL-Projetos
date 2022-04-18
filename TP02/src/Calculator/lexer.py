"""lexer.py: Ficheiro onde está definido o lexer da linguagem associada a uma calculadora"""

import sys
sys.path.append('../')
from ply import lex


tokens = (
            "VAR", 
            "NUMBER",
        )

literals = [    '+',
                '-',
                '*',
                '/',
                '(',
                ')',
                '='
            ]

t_ignore = " \t\n"

def t_VAR(t):
    r'[A-Za-z_][a-zA-Z0-9_]*'
    #print("- var [" + t.value + "] - lineno: " + str(t.lexer.lineno))
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    #print ("- int [" + t.value + "] - lineno: " + str(t.lexer.lineno))
    t.value = float(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)

lexer = lex.lex()


# ----------------------------------------------------------------------------------
#import sys
#
#for line in sys.stdin:
#
#    lexer.input(line)
#    tokens = [x.value for x in lexer]
#    lexer.lineno = lexer.lineno + 1





