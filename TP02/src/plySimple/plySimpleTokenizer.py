"""simplePlyTokenizer.py : Ficheiro com todos os tokens definidos para captar num ficheiro de Ply-Simple."""

import sys
sys.path.append('../')
from ply import lex
import re

class PlySimpleTokenizer:

    ### https://www.dabeaz.com/ply/ply.html
    ## When building a lexer from class, you should construct the lexer from an instance of the class, not the class object itself.
    ## This is because PLY only works properly if the lexer actions are defined by bound-methods.

    def build(my):
        my.lexer = lex.lex(module=my)
        my.lexer.begin('LEX')
        my.lexer.squareBracket = 0
        my.lexer.roundBracket = 0
        my.lexer.brackets = 0
        my.lexer.lineno = 0

    states = (
        ('LEX', 'inclusive'),                   # estado utilizado para captar lex tokens
        ('YACC', 'inclusive'),                  # estado utilizado para captar yacc tokens
        ('GRULE', 'inclusive'),
        ('FREEPYTHON', 'inclusive')             # estado FREE para captar qualquer coisa que seja código python
    )
    
    tokens = (
        
        #   - states -
        "LEXSTATE",             ## %%LEX
        "YACCSTATE",            ## %%YACC
        "FREESTATE",            ## %%
        
        #   - LEX init -
        "LITERALS",             # literals
        "IGN",                  # ignore
        "CHARS",                # "+-*/"
        "TKNS",                 # tokens
        "VAR",                  # 'VARNAME'
        "STATES",
        "INCLUSIVE",
        "EXCLUSIVE",

        #   - LEX return -
        "REGEX",                # regex format
        "RETURN",               # return
        "PLYTVALUE",            # t.value
        "RETTYPE",              # int, float, list, set
        "RETSTATE",             # $STATENAME
        "ERROR",                # error
        "FSTR",                 # f"something"
        "TSKIP",                # t.lexer.skip(int)

        #   - YACC -
        "PRECEDENCE",           # %precedence
        "LEFT",                 # left
        "RIGHT",                # right
        "PRECTOKEN",            # precedence tokens = '+', 'UMINUS'

        "RULENAME",             # name of the rule = stat : ...

        #   - GRULE -
        "RULEFORMAT",           # rule's format
        "RULECODE",             # rule code inside brackets = { code }


        #   - FREE PYTHON MODE -
        "PYTHON",               # anything : python code


        #   - COMMON -
        "COMMENT",              # python's comment signature
        "OPSQUAREB",            # '['
        "CLSQUAREB",            # ']'
        "OPCURVEB",             # '('
        "CLCURVEB",             # ')'
    )

    literals = [

        ',',
        '\"',
        '\'',
        '%',
        '=',
    ]

    # ------------------------------------------------------------------- IGNORE
    t_LEX_ignore = " \t\r"
    t_YACC_ignore = " \t\r"
    t_GRULE_ignore = " \t\r"
    t_FREEPYTHON_ignore = ""
    t_ignore = " \r\t"

    def t_ignore_newline(my, t):
        r'\n'
        t.lexer.lineno += 1


    # ------------------------------------------------------------------- STATES IDENTIFIERS
    # lexstate, "%%lex", case insensitive
    def t_LEXSTATE(my, t):
        r'%%\s*(?i:lex)'
        t.value = t.value.upper()
        t.lexer.begin('LEX')
        return t
        #print("\n#> STATE CHANGE : [LEX STATE]")

    # staccstate, "%%yacc", case insensitive
    def t_YACCSTATE(my, t):
        r'%%\s*(?i:yacc)'
        t.value = t.value.upper()
        t.lexer.begin('YACC')
        return t
        #print("\n#> STATE CHANGE : [YACC STATE]")

    # freepython, "%%"
    def t_FREESTATE(my, t):
        r'%%\s*\n?'
        t.lexer.begin('FREEPYTHON')
        return t
        #print("\n#> STATE CHANGE : [FREE STATE]")


    # ------------------------------------------------------------------- LEX STATE RULES
    
    ## identify "error"
    def t_LEX_ERROR(my, t):
        r'error'
        return t

    ## identify a formatted string, f"..."
    def t_LEX_FSTR(my, t):
        r'f\s*\".*\"'
        #print("string format: " + t.value)
        return t

    ## identify t.lexer.skip(INT)
    def t_LEX_TSKIP(my, t):
        r't\.lexer\.skip\(\d+\)'
        #print("skip: " + t.value)
        return t

    ## identify a return type : float, int, list, set
    def t_LEX_RETTYPE(my, t):
        r'float\s*|int\s*|list\s*|set\s*'
        #print("return type: " + t.value)
        return t

    ## identify "t.value"
    def t_LEX_PLYTVALUE(my, t):
        r't.value'
        #print("TVALUE: " + t.value)
        return t

    ## 'inclusive'
    def t_LEX_INCLUSIVE(my, t):
        r'\'(?i:inclusive)\''
        t.value = t.value.lower()
        #print("inclusive: " + t.value)
        return t
    
    ## 'exclusive'
    def t_LEX_EXCLUSIVE(my, t):
        r'\'(?i:exclusive)\''
        t.value = t.value.lower()
        #print("exclusive:" + t.value)
        return t

    ## identify a variable given as a token for ply : 'VARNAME'
    def t_LEX_VAR(my, t):
        r'\'[^\W]+\''
        #t.value = t.value[1:-1]
        #print("VAR :: " + t.value)
        return t

    ## identify a token's regex
    def t_LEX_REGEX(my, t):
        r'\'.+\'\s+'
        t.value = t.value.split("\'")[1]
        #print("\nREGEX: " + t.value, end="\n")
        return t

    ## identify "literals", case insensitive
    def t_LEX_LITERALS(my, t):
        r'(?i:literals)'
        t.value = t.value.lower()
        #print("LITERALS: " + t.value)
        return t

    ## identify "ignore", case insensitive
    def t_LEX_IGN(my, t):
        r'(?i:ignore)'
        t.value = t.value.lower()
        #print("IGNORE")
        return t

    ## identify "tokens", case insensitive
    def t_LEX_TKNS(my, t):
        r'(?i:tokens)'
        t.value = t.value.lower()
        #print("TOKENS: " + t.value)
        return t

    ## %state
    def t_LEX_STATES(my,t):
        r'(?i:states)'
        t.value = t.value.lower()
        #print("states: " + t.value)
        return t


    ## identify "return", case insensitive
    def t_LEX_RETURN(my, t):
        r'return'
        #print("RETURN: " + t.value)
        return t

    def t_LEX_RETSTATE(my, t):
        r'\$\s*[^ ),\']+'
        t.value = t.value[1:]
        #print("return state: " + t.value)
        return t

    ## identify a sequence of chars given for %literals and %ignore
    def t_LEX_CHARS(my, t):
        r'\"[^\"]+\"'
        t.value = t.value[1:-1]
        #print("CHARS :: " + t.value)
        return t

# ------------------------------------------------------------------- YACC STATE RULES
    
    ### "%precedence", case insensitive
    def t_YACC_PRECEDENCE(my, t):
        r'precedence'
        #print("PRECEDENCE :: " + t.value)
        return t

    ### 'left', case insensitive
    def t_YACC_LEFT(my, t):
        r'\'(?i:left)\''
        t.value = t.value.lower()
        #print("LEFT :: " + t.value)
        return t

    ### 'right', case insensitive
    def t_YACC_RIGHT(my, t):
        r'\'(?i:right)\''
        t.value = t.value.lower()
        #print("RIGHT :: " + t.value)
        return t

    ### yacc production rule's name, "stat :"
    def t_YACC_RULENAME(my, t):
        r'\w+\s+:'
        split = t.value.split(" ")
        t.value = split[0]
        t.lexer.begin('GRULE')
        return t

    ### yacc production rule's format, " ..." { code
    def t_GRULE_RULEFORMAT(my, t):
        r' (.+){'
        catcher = re.compile(r'.+\w')
        t.value = catcher.match(t.value).group()
        #print("RULE: \"" + t.value + "\"")
        return t
    
    ### yacc production rule's python code, { code }
    def t_GRULE_RULECODE(my, t):
        r'(.+)}'
        t.value = t.value[:-1]
        catcher = re.compile(r'\s*(.+)\s*')
        #print("RULECODE : \"" + t.value + "\"")
        t.value = catcher.match(t.value).group()
        t.lexer.begin('YACC')
        return t



    ### precedence tokens = '+', 'UMINUS', etc
    def t_YACC_PRECTOKEN(my, t):
        r'\'[^\']+\''
        #print("PRECTOKEN :: " + t.value)
        return t

    

    # ------------------------------------------------------------------- COMMON STATE RULES

    ## open square brackets, '['
    def t_OPSQUAREB(my, t):
        r'\['
        t.lexer.squareBracket = t.lexer.squareBracket + 1 
        return t
    
    ## close square brackets, ']'
    def t_CLSQUAREB(my, t):
        r']'
        if t.lexer.squareBracket > 0:
            t.lexer.squareBracket = t.lexer.squareBracket - 1 
        return t

    ## open curve brackets, '('
    def t_OPCURVEB(my, t):
        r'\('
        t.lexer.roundBracket = t.lexer.roundBracket + 1 
        return t
    
    ## close curve brackets, ')'
    def t_CLCURVEB(my, t):
        r'\)'
        if t.lexer.roundBracket > 0:
            t.lexer.roundBracket = t.lexer.roundBracket - 1 
        return t

    

    # comment statement, # ...
    def t_COMMENT(my, t):
        r'\#[^\r]*'
        split = t.value.split('\r\n')
        t.value = split[0]
        return t


    # ------------------------------------------------------------------- FREE STATE RULES
    def t_PYTHON(my, t):
        r'[^%\'"#=,].+'
        #print("python: " + t.value)
        return t

    def t_FREEPYTHON_PYTHON(my, t):
        r'[^%\'"#=,].+'
        return t

    def t_error(my, t):
        print("Illegal char: '%s'" % t.value[0])
        t.lexer.skip(1)


    """insideMultiline : Verifica se algum tipo de parênteses foi aberto, mas ainda não foi fechado
            
            3 tipos de parênteses:
            - squareBracket : '['
            - roundBracket : '('
            - brackets : '{'
    """
    def insideMultiline(my):

        if my.lexer.squareBracket != 0: return True
        elif my.lexer.roundBracket != 0: return True
        elif my.lexer.brackets != 0: return True
        else: return False