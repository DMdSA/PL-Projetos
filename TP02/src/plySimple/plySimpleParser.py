""""""


import sys
sys.path.append('../')
from ply import yacc

from plySimpleTokenizer import PlySimpleTokenizer
from plySimpleLex import *
from plySimpleYacc import *

pythonCode_key = "pythonCode"

class PlySimpleParser:

    def __init__(self, lexObject, yaccObject):

        self._tokenizer = PlySimpleTokenizer()      ## tokenizer
        self._tokenizer.build()                     ## build tokenizer
        self._parser = yacc.yacc(module=self)       ## parser
        self._yaccObject = yaccObject               ## yacc object
        self._lexObject = lexObject                 ## lex object
        

    
    ## tokenizer
    @property
    def tokenizer(my):
        return my._tokenizer

    @tokenizer.setter
    def tokenizer(my, value):
        my._tokenizer = value

    @tokenizer.deleter
    def tokenizer(my):
        del my._tokenizer
    

    ## get tokens from tokenizer
    tokens = PlySimpleTokenizer.tokens
    start = "start"

    ##START OPTIONS
    ##-------------------------------------------------------------- GRAMMAR START
    ##-------------------------------------- LEX START
    
    def p_start_init(my, p):
        "start : init"
        p[0] = p[1]

    def p_start_regexRules(my, p):
        "start : regexRules"
        p[0] = p[1]
    
    def p_start_states(my, p):
        "start : states"
        p[0] = p[1]

    ##-------------------------------------- YACC START

    # precedence statement
    def p_start_precedence(my, p):
        "start : precedence"
        p[0] = p[1]
    
    # production rules
    def p_start_productionRules(my, p):
        "start : productionRules"
        p[0] = p[1]
    

    ##-------------------------------------- FREE START

    ## usual python code
    def p_start_pythonCode(my, p):
        "start : pythonCode"
        p[0] = p[1]


    ##-------------------------------------- COMMON START

    def p_start_changeLex(my, p):
        "start : LEXSTATE comment"
        my._tokenizer.lexer.begin('LEX')

    def p_start_changeYacc(my, p):
        "start : YACCSTATE comment"
        my._tokenizer.lexer.begin('YACC')
        print("\n#> YACC STATE")
    
    def p_start_changeFree(my, p):
        "start : FREESTATE comment"
        my._tokenizer.lexer.begin('FREEPYTHON')
        print("\n#> FREE STATE")

    # comments
    def p_start_comment(my, p):
        "start : comment"
        p[0] = p[1]
        comment = {comment_key : p[0], lineno_key : my._tokenizer.lexer.lineno}
        my._yaccObject.addStatement(comment)

    # FIM
    def p_start_fim(my, p):
        "start : "

    

    ##-------------------------------------------------------------- LEX GRAMMAR
    ## INITIALIZE PLY

    # %literals = "+-,"
    def p_init_LITERALS(my, p):
        "init : '%' LITERALS '=' CHARS comment"
        lit = {p[2] : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[5]}
        print(lit)
        my._lexObject.addStatement(lit)
        #my._lexObject.printVariables()

    # %ignore = " \n\t\r"
    def p_init_IGNORE(my, p):
        "init : '%' IGN '=' CHARS comment"
        ign = {p[2] : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[5]}
        print(ign)
        my._lexObject.addStatement(ign)
        #my._lexObject.printVariables()
        #print("\n" + str(plyDictionary))

    # extra: railing comma acceptance, %tokens = [ 'VARNAME' ,]
    def p_init_tokens_railing(my, p):
        "init : '%' TKNS '=' OPSQUAREB vars ',' CLSQUAREB comment"
        tks = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
        print(tks)
        my._lexObject.addStatement(tks)
        #my._lexObject.printVariables()

    # %tokens = [ 'VARNAME01', 'VARNAME02', ...]
    def p_init_tokens(my, p):
        "init : '%' TKNS '=' OPSQUAREB vars CLSQUAREB comment"
        tks = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        print(tks)
        my._lexObject.addStatement(tks)
        #my._lexObject.printVariables()

    #! def p_init_fim(my, p):
    #!     "init : "
    
    # ... , 'VARNAME'
    def p_vars_variaveis(my, p):
        "vars : vars ',' VAR"
        p[0] = p[1] + [p[3]]

    # 'VARNAME'
    def p_vars_var(my, p):
        "vars : VAR"
        p[0] = [p[1]]


    ## STATES RULES

    # state extra form railing comma (python alike!)
    def p_states_railing(my, p):
        "states : '%' STATES '=' OPCURVEB stateStatements ',' CLCURVEB comment"
        st = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
        print(st)
        p[0] = st
        my._lexObject.addStatement(st)

    # state format
    def p_states(my, p):
        "states : '%' STATES '=' OPCURVEB stateStatements CLCURVEB comment"
        st = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        print(st)
        p[0] = st
        my._lexObject.addStatement(st)    
    
     # state : two statements (maximum allowed)
    def p_stateStatements_two(my, p):
        "stateStatements : state ',' state"
        p[0] = list() + [p[1]] + [p[3]]

    # state : one and only one statement
    def p_stateStatements_unique(my, p):
        "stateStatements : state"
        p[0] = [p[1]]

    # state INCLUSIVE
    def p_state_inclusive(my, p):
        "state : VAR ',' INCLUSIVE"
        p[0] = (p[2], p[4])

    # state EXLCUSIVE
    def p_state_exclusive(my, p):
        "state : VAR ',' EXCLUSIVE"
        p[0] = (p[2], p[4])








    ## REGEX RULES 

    # '[a-zA-Z]'     return(...) 
    def p_regexRules_regex_regex(my, p):
        "regexRules : REGEX RETURN OPCURVEB regexReturn CLCURVEB comment"
       # print("regex01: " + p[1] + ", " + "return: " + str(p[4]))

        variavel = (p[4])[0]
        tipo = (p[4])[1]
        ret = {return_key : variavel, variavel : tipo, regex_key : p[1], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        print(ret)
        my._lexObject.addStatement(ret)
        #my._lexObject.printVariables()

    # alternative for latter rule, when regex is mistaken for a VAR
    def p_regexRules_regex_var(my, p):
        "regexRules : VAR RETURN OPCURVEB regexReturn CLCURVEB comment"
        #print("regex02: " + p[1] + ", " + "return: " + str(p[4]))

        variavel = (p[4])[0]
        tipo = (p[4])[1]
        ret = {return_key : variavel, variavel : tipo, regex_key : p[1], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        print(ret)
        my._lexObject.addStatement(ret)
        #my._lexObject.printVariables()

    # error (...)
    def p_regexRules_error(my, p):
        "regexRules : errorRules comment"
        p[0] = p[1]
        err = {error_key : p[0], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[2]}
        print(err)
        my._lexObject.addStatement(err)

    # return('VARNAME')
    def p_regexReturn_var(my, p):
        "regexReturn : VAR"
        p[0] = (p[1], "str")

    # return('VARNAME' , t.value)
    def p_regexReturn_varresult(my, p):
        "regexReturn : VAR ',' PLYTVALUE"
        p[0] = (p[1], p[3])

    # return('VARNAME' , float(t.value))
    def p_regexReturn_vartype(my, p):
        "regexReturn : VAR ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB"
        p[0] = (p[1], p[3])

    # '.' error(...)
    def p_errorRules(my, p):
        "errorRules : REGEX ERROR OPCURVEB errorValues CLCURVEB"
        p[0] = p[4]

    # f"..."
    def p_errorValuesFSTR(my, p):
        "errorValues : FSTR"
        p[0] = p[1]
        # o resultado é apenas uma string formatada

    # t.lexer.skip(INT)
    def p_errorValuesSkip(my, p):
        "errorValues : TSKIP"
        p[0] = p[1]

    # (f"..." , t.lexer.skip)
    def p_errorValuesMoreV1(my, p):
        "errorValues : FSTR ',' TSKIP"
        p[0] = (p[1], p[3])

    # (t.lexer.skip, f"..."")
    def p_errorValuesMoreV2(my, p):
        "errorValues : TSKIP ',' FSTR"
        p[0] = (p[3], p[1])

    
    ##-------------------------------------------------------------- YACC GRAMMAR

    # PRECEDENCE

    # precedence extra form railing comma (python alike!)
    def p_precedence_railing(my, p):
        "precedence : PRECEDENCE '=' OPSQUAREB precStatements ',' CLSQUAREB comment"
        p[0] = p[4]
        precedence = {p[1] : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        print(precedence)
        my._yaccObject.addStatement(precedence)

    # precedence format
    def p_precedence(my, p):
        "precedence : PRECEDENCE '=' OPSQUAREB precStatements CLSQUAREB comment"
        p[0] = p[4]
        precedence = {p[1] : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        print(precedence)
        my._yaccObject.addStatement(precedence)    
    
    # precedence : one and only one statement
    def p_precStatements_unique(my, p):
        "precStatements : precStatement"
        p[0] = [p[1]]

    # precedence : more than one statement
    def p_precStatements_list(my, p):
        "precStatements : precStatements ',' precStatement"
        p[0] = p[1] + [p[3]]
    
    
    # precedence left tokens
    def p_precStatement_left(my, p):
        "precStatement : OPCURVEB LEFT ',' precTokens CLCURVEB"
        p[0] = (p[2], p[4])

    # precedence right tokens
    def p_precStatement_right(my, p):
        "precStatement : OPCURVEB RIGHT ',' precTokens CLCURVEB"
        p[0] = (p[2], p[4])
    
    
    # one and only one PREC TOKEN ex: ("left", "+")
    def p_precTokens(my, p):
        "precTokens : PRECTOKEN"
        p[0] = [p[1]]
    
    # more than one PREC TOKEN ex: ("left", "+", "-")
    def p_precTokens_list(my, p):
        "precTokens : precTokens ',' PRECTOKEN"
        p[0] = p[1] + [p[3]]


    # PRODUCTION RULES

    def p_productionRules(my, p):
        "productionRules : RULENAME RULEFORMAT OPBRACKETS RULECODE CLBRACKETS comment"
        rule = {prodRule_key : p[1], p[1] : p[2], pythonCode_key : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        p[0] = rule
        print(rule)
        my._yaccObject.addStatement(rule)


    ##-------------------------------------------------------------- FREE GRAMMAR
    
    # python code
    def p_pythonCode(my, p):
        "pythonCode : PYTHON"
        python = {pythonCode_key : p[1], lineno_key : my._tokenizer.lexer.lineno}
        p[0] = python
        print(python)
        my._yaccObject.addStatement(python)

    

    ##-------------------------------------------------------------- COMMON GRAMMAR

    ## -----------------------
    # COMMENTS & ERROR
    ## -----------------------

    def p_comment(my, p):
        "comment : COMMENT"
        p[0] = p[1]

    def p_comment_fim(my, p):
        "comment : "
        p[0] = ""

    ## PARSER ERROR
    def p_error(my, p):
        print(f"Syntax error at '{p.value}', {p}")


from plySimpleYacc import PlySYaccObject
psLexObject = PlySLexObject()
psYaccObject = PlySYaccObject()
psParser = PlySimpleParser(psLexObject, psYaccObject)

tokenizer = psParser._tokenizer
lexer = tokenizer.lexer
auxString = ""

fHandler = open("lexteste.txt", "rt", encoding="utf-8")
for line in fHandler:

    lexer.input(line)
    [x.value for x in lexer]

    auxString = auxString + line
    if tokenizer.insideMultiline() is False:
        psParser._parser.parse(auxString)
        auxString = ""
    
fHandler.close()

psLexObject.printVariables()