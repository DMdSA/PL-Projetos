""""""


import sys
sys.path.append('../')
from ply import yacc

from plySimple.plySimpleTokenizer import PlySimpleTokenizer
from plySimple.plySimpleLex import *
from plySimple.plySimpleYacc import *

lexState = "LEX"
yaccState = "YACC"
freeState = "FREE"

class PlySimpleParser:

    def __init__(self, lexObject, yaccObject):

        self._tokenizer = PlySimpleTokenizer()      ## tokenizer
        self._tokenizer.build()                     ## build tokenizer
        self._parser = yacc.yacc(module=self)       ## parser
        self._yaccObject = yaccObject               ## yacc object
        self._lexObject = lexObject                 ## lex object
        self._currentState = lexState
        

    
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
    literals = PlySimpleTokenizer.literals
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
        p.lexer.begin('LEX')
        my._currentState = lexState
        p[0] = {"LEXSTATE" : p[1], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[2]}

    def p_start_changeYacc(my, p):
        "start : YACCSTATE comment"
        p.lexer.begin('YACC')
        my._currentState = yaccState
        #print("\n#> YACC STATE")
        p[0] = {"YACCSTATE" : p[1], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[2]}
    
    def p_start_changeFree(my, p):
        "start : FREESTATE comment"
        p.lexer.begin('FREEPYTHON')
        my._currentState = freeState
        #print("\n#> FREE STATE")
        p[0] = {"FREESTATE" : p[1], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[2]}

    # comments
    def p_start_comment(my, p):
        "start : comment"
        comment = {comment_key : p[1], lineno_key : my._tokenizer.lexer.lineno}
        p[0] = comment
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
        p[0] = lit
        #print(lit)
        my._lexObject.addStatement(lit)
        #my._lexObject.printVariables()

    # %ignore = " \n\t\r"
    def p_init_IGNORE(my, p):
        "init : '%' IGN '=' CHARS comment"
        ign = {p[2] : p[4], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[5]}
        p[0] = ign
        #print(ign)
        my._lexObject.addStatement(ign)
        #print("\n" + str(plyDictionary))

    # extra: railing comma acceptance, %tokens = [ 'VARNAME' ,]
    def p_init_tokens_railing(my, p):
        "init : '%' TKNS '=' OPSQUAREB vars ',' CLSQUAREB comment"
        tks = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
        p[0] = tks
        #print(tks)
        my._lexObject.addStatement(tks)
        #my._lexObject.printVariables()

    # %tokens = [ 'VARNAME01', 'VARNAME02', ...]
    def p_init_tokens(my, p):
        "init : '%' TKNS '=' OPSQUAREB vars CLSQUAREB comment"
        tks = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        p[0] = tks
        #print(tks)
        my._lexObject.addStatement(tks)
        #my._lexObject.printVariables()

    
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
        "states : '%' STATES '=' OPSQUAREB stateStatements ',' CLSQUAREB comment"
        st = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
        #print(st)
        p[0] = st
        my._lexObject.addStatement(st)

    # state format
    def p_states(my, p):
        "states : '%' STATES '=' OPSQUAREB stateStatements CLSQUAREB comment"
        st = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        print(st)
        p[0] = st
        my._lexObject.addStatement(st)    
    
    def p_stateStatementsList(my, p):
        "stateStatements : stateStatements ',' state"
        p[0] = p[1] + [p[3]]
    
    def p_statements(my, p):
        "stateStatements : state"
        p[0] = [p[1]]

    # state INCLUSIVE
    def p_state_inclusive(my, p):
        "state : OPCURVEB VAR ',' INCLUSIVE CLCURVEB"
        p[0] = (p[2], p[4])

    # state EXLCUSIVE
    def p_state_exclusive(my, p):
        "state : OPCURVEB VAR ',' EXCLUSIVE CLCURVEB"
        p[0] = (p[2], p[4])




    ## REGEX RULES 

    # '[a-zA-Z]'     return(...)
    def p_regexRules_regex_regex(my, p):
        "regexRules : REGEX RETURN OPCURVEB regexReturn CLCURVEB comment"
        variavel = (p[4])[0]
        tipo = (p[4])[1]
        state = (p[4])[2]
        ret = {return_key : variavel, variavel : tipo, regex_key : p[1], states_key : state, lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        p[0] = ret
        #print(ret)
        my._lexObject.addStatement(ret)

    # alternative for latter rule, when regex is mistaken for a VAR
    def p_regexRules_regex_var(my, p):
        "regexRules : VAR RETURN OPCURVEB regexReturn CLCURVEB comment"
        variavel = (p[4])[0]
        tipo = (p[4])[1]
        state = (p[4])[2]
        ret = {return_key : variavel, variavel : tipo, regex_key : p[1], states_key : state, lineno_key : my._tokenizer.lexer.lineno, comment_key : p[6]}
        my._lexObject.addStatement(ret)
        p[0] = ret

    # error (...)
    def p_regexRules_error(my, p):
        "regexRules : errorRules comment"
        p[0] = p[1]
        err = {error_key : p[0], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[2]}
        #print(err)
        my._lexObject.addStatement(err)



    # return('VARNAME')
    def p_regexReturn_onlyvar(my, p):
        "regexReturn : VAR"
        p[0] = (p[1], "str", None)

    # return('VARNAME' , t.value)
    def p_regexReturn_varvalue(my, p):
        "regexReturn : VAR ',' PLYTVALUE"
        p[0] = (p[1], p[3], None)
    
    # return('VAR', $statename)
    def p_regexReturn_varState(my, p):
        "regexReturn : VAR ',' RETSTATE"
        p[0] = (p[1], "str" , p[3])

    # return('VAR', float(t.value))
    def p_regexReturn_vartype(my, p):
        "regexReturn : VAR ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB"
        p[0] = (p[1], p[3], None)

    # return('VAR', t.value, $state)
    def p_regexReturn_varValueState(my, p):
        "regexReturn : VAR ',' PLYTVALUE ',' RETSTATE"
        p[0] = (p[1], p[3], p[5])

    # return('VAR', $state, t.value)
    def p_regexReturn_varStateValue(my, p):
        "regexReturn : VAR ',' RETSTATE ',' PLYTVALUE"
        p[0] = (p[1], p[5], p[3])

    # return('VAR' , list(t.value) , $state)
    def p_regexReturn_varTypeState(my, p):
        "regexReturn : VAR ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB ',' RETSTATE"
        p[0] = (p[1], p[3], p[8])
    
    # return('VAR', $state, float(t.value))
    def p_regexReturn_varStateType(my, p):
        "regexReturn : VAR ',' RETSTATE ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB"
        p[0] = (p[1], p[5], p[3])


    # return(t.value, 'VARNAME')
    def p_regexReturn_valueVar(my, p):
        "regexReturn : PLYTVALUE ',' VAR"
        p[0] = (p[3], p[1], None)

    # return(t.value, 'VAR', $state)
    def p_regexReturn_valueVarState(my, p):
        "regexReturn : PLYTVALUE ',' VAR ',' RETSTATE"
        p[0] = (p[3], p[1], p[5])
    
    # return(t.value, $state, 'VAR')
    def p_regexReturn_valueStateVar(my, p):
        "regexReturn : PLYTVALUE ',' RETSTATE ',' VAR"
        p[0] = (p[5], p[1], p[3])


    # return(float(t.value), 'VARNAME')
    def p_regexReturn_typeVar(my, p):
        "regexReturn : RETTYPE OPCURVEB PLYTVALUE CLCURVEB ',' VAR"
        p[0] = (p[6], p[1], None)

    # return(float(t.value), 'VAR', $state)
    def p_regexReturn_typeVarState(my ,p):
        "regexReturn : RETTYPE OPCURVEB PLYTVALUE CLCURVEB ',' VAR ',' RETSTATE"
        p[0] = (p[6], p[1], p[8])

    # return(list(t.value), $state, 'VAR')
    def p_regexReturn_typeStateVar(my, p):
        "regexReturn : RETTYPE OPCURVEB PLYTVALUE CLCURVEB ',' RETSTATE ',' VAR"
        p[0] = (p[8], p[1], p[6])


    # return($state, 'VAR')
    def p_regexReturn_stateVar(my, p):
        "regexReturn : RETSTATE ',' VAR"
        p[0] = (p[3], "str", p[1])
    
    # return($state, 'VAR', t.value)
    def p_regexReturn_stateVarValue(my, p):
        "regexReturn : RETSTATE ',' VAR ',' PLYTVALUE"
        p[0] = (p[3], p[5], p[1])

    # return ($state, 'VAR', float(t.value))
    def p_regexReturn_stateVarType(my, p):
        "regexReturn : RETSTATE ',' VAR ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB"
        p[0] = (p[3], p[5], p[1])

    # return($state, t.value, 'VAR')
    def p_regexReturn_stateValueVar(my, p):
        "regexReturn : RETSTATE ',' PLYTVALUE ',' VAR"
        p[0] = (p[5], p[3], p[1])

    def p_regexReturn_stateTypeVar(my, p):
        "regexReturn : RETSTATE ',' RETTYPE OPCURVEB PLYTVALUE CLCURVEB ',' VAR"
        p[0] = (p[8], p[3], p[1])



    # '.' error(...)
    def p_errorRules(my, p):
        "errorRules : REGEX ERROR OPCURVEB errorValues CLCURVEB"
        p[0] = p[4]


    def p_errorValuesFSTRRailling(my, p):
        "errorValues : FSTR ','"
        p[0] = (p[1], )
        # o resultado é apenas uma string formatada

    # f"..."
    def p_errorValuesFSTR(my, p):
        "errorValues : FSTR"
        p[0] = (p[1], )
        # o resultado é apenas uma string formatada

    def p_errorValuesSkipRailling(my, p):
        "errorValues : TSKIP ','"
        p[0] = (p[1], )

    # t.lexer.skip(INT)
    def p_errorValuesSkip(my, p):
        "errorValues : TSKIP"
        p[0] = (p[1], )

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
        "precedence : '%' PRECEDENCE '=' OPSQUAREB precStatements ',' CLSQUAREB comment"
        precedence = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
        p[0] = precedence
        #print(precedence)
        my._yaccObject.addStatement(precedence)

    # precedence format
    def p_precedence(my, p):
        "precedence : '%' PRECEDENCE '=' OPSQUAREB precStatements CLSQUAREB comment"
        precedence = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[7]}
        p[0] = precedence
        #print(precedence)
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
        #"productionRules : RULENAME RULEFORMAT OPBRACKETS RULECODE CLBRACKETS comment"
        "productionRules : RULENAME format"
        #p.lexer.begin('GRULE')

        rule = {prodRule_key : p[1], p[1] : (p[2])[0]}
        rule.update((p[2])[1])
        p[0] = rule
        my._yaccObject.addStatement(rule)


    def p_ruleFormat(my, p):
        "format : RULEFORMAT RULECODE comment"
        p.lexer.begin('YACC')
        p[0] = (p[1], {python_key : p[2], lineno_key: my._tokenizer.lexer.lineno, comment_key : p[3]})




    ##-------------------------------------------------------------- FREE GRAMMAR
    
    # python code
    def p_pythonCode(my, p):
        "pythonCode : PYTHON"
        python = {python_key : p[1], lineno_key : my._tokenizer.lexer.lineno}
        p[0] = python
        #print(python)
        if p[1] != "%%":
            if my._currentState == lexState:
                my._lexObject.addStatement(python)
            else:
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
        if p:
            print(f"Syntax error at '{p.value}', {p}")
        else:
            print("\n#> error parsing object: None")


# está a funcionar
#from plySimpleYacc import PlySYaccObject
#psLexObject = PlySLexObject()
#psYaccObject = PlySYaccObject()
#psParser = PlySimpleParser(psLexObject, psYaccObject)
#
#tokenizer = psParser._tokenizer
#lexer = tokenizer.lexer
#auxString = ""
#
#fHandler = open("lexteste.txt", "rt", encoding="utf-8")
#for line in fHandler:
#
#    lexer.input(line)
#    [x.value for x in lexer]
#
#    auxString = auxString + line
#    if tokenizer.insideMultiline() is False:
#        psParser._parser.parse(auxString)
#        auxString = ""
#    
#fHandler.close()
#
#psLexObject.printVariables()