"""plySLexer.py: Definição de um tokenizer utilizado para configuração do PlySimple"""

import sys
sys.path.append('../')
from ply import lex


tokens = (

    #"LEXSTATE",             ## %%LEX
    #"YACCSTATE",            ## %%YACC

    "LITERALS",             # literals = "+-"
    "IGN",                  # ignore = " \n\r\t"
    "CHARS",                # "+-*/"
    "TKNS",                 # tokens = [ 'VARNAME', ...]
    "VAR",                  # 'VARNAME'

    "REGEX",                # regex format
    "RETURN",               # return
    "PLYTVALUE",            # t.value
    "RETTYPE",              # int, float, list, set
    "ERROR",                # error
    "FSTR",                 # f"something"
    "TSKIP",                # t.lexer.skip(int)

    "COMMENT",              # python's comment signature

)

literals = [

    '[', ']',
    '(', ')',
    ',',
    '\"',
    '\'',
    '%',
    '='
]

t_ignore = " \t"


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ERROR(t):
    r'error'
    return t

def t_FSTR(t):
    r'f\s*\".*\"'
    return t

def t_TSKIP(t):
    r't\.lexer\.skip\(\d+\)'
    return t

def t_RETTYPE(t):
    r'float\s*|int\s*|list\s*|set\s*'
    return t

def t_PLYTVALUE(t):
    r't.value'
    #print("TVALUE")
    return t

def t_LEXSTATE(t):
    r'%%(?i:lex)'
    t.value = t.value.upper()
    return t

def t_YACCSTATE(t):
    r'%%(?i:yacc)'
    t.value = t.value.upper()
    return t


def t_VAR(t):
    r'\'[^\W]+\''
    t.value = t.value[1:-1]
    #print("VAR :: " + t.value)
    return t

def t_REGEX(t):
    r'\'.+\'\s+'
    t.value = t.value.split("\'")[1]
    #print("\nREGEX: " + t.value, end="\n")
    return t


def t_LITERALS(t):
    r'(?i:literals)'
    t.value = t.value.lower()
    #print("LITERALS")
    return t

def t_IGN(t):
    r'(?i:ignore)'
    t.value = t.value.lower()
    #print("IGNORE")
    return t

def t_TKNS(t):
    r'(?i:tokens)'
    t.value = t.value.lower()
    #print("TOKENS")
    return t

def t_RETURN(t):
    r'return'
    #print("RETURN")
    return t

def t_CHARS(t):
    r'\".+\"'
    t.value = t.value[1:-1]
    #print("CHARS :: " + t.value)
    return t

def t_COMMENT(t):
    r'\#.*\n$'
    t.value = t.value[:-1]
    return t

def t_error(t):
    print("Illegal char: '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()

#for line in sys.stdin:
#
#    lexer.input(line)
#    tks = [x.value for x in lexer]
#    print(tks)