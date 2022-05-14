
from plySimple.plySimpleLex import PlySLexObject
from plySimple.plySimpleYacc import PlySYaccObject
from plySimple.plySimpleParser import PlySimpleParser
import sys

## lex keys
from plySimple.plySimpleLex import tokens_key, definedToken_key, literals_key, ignore_key, error_key, return_key, regex_key, states_key
## yacc keys (2) + common ones (4)
from plySimple.plySimpleYacc import precedence_key, prodRule_key, lineno_key, comment_key, id_key, python_key


PTAB = '\t'     # python tab

class PlySimple:

    def __init__(self, filename):
        
        self._filename = filename
        self._lexObject = PlySLexObject()       # lex object
        self._yaccObject = PlySYaccObject()     # yacc object

    ##--------------------------------------------------
    ##----------------- Variables gets/sets/deleters ---
    ##--------------------------------------------------
    
    ## filename
    @property
    def filename(my):
        return my._filename
    
    @filename.setter
    def filename(my, value):
        my._filename = value
    
    @filename.deleter
    def filename(my):
        del my._filename

    
    ## lexObject
    @property
    def lexObject(my):
        return my._lexObject
    
    @lexObject.setter
    def lexObject(my, value):
        my._lexObject = value
    
    @lexObject.deleter
    def lexObject(my):
        del my._lexObject

    
    ## yaccObject
    @property
    def yaccObject(my):
        return my._yaccObject
    
    @yaccObject.setter
    def yaccObject(my, value):
        my._yaccObject = value
    
    @yaccObject.deleter
    def yaccObject(my):
        del my._yaccObject
    





    """Lê e captura toda a gramática reconhecida num ficheiro de texto com PlySimple"""
    def readPlySimple(my):
    
        parser = PlySimpleParser(my._lexObject, my._yaccObject)
        tokenizer = parser._tokenizer
        lexer = tokenizer.lexer
        auxString = ""
        fHandler = open(my._filename, "rt", encoding="utf-8")
        for line in fHandler:
        
            lexer.input(line)
            [x.value for x in lexer]
            auxString = auxString + line

            if tokenizer.insideMultiline() is False:
                #print("FRASE:\"" + auxString + "\"")
                parser._parser.parse(auxString)
                auxString = ""

        fHandler.close()


    def transcribe_plySimple(my):
        my.transcribe_lex_sorted()
        my.transcribe_yacc_sorted()


    """Transcreve um comentário, caso exista"""
    def transc_stat_comment(my, something):
        
        if len(something[comment_key]) > 0:
            print(something[comment_key])

    def transc_comment(my, comment):

        print(comment)


    """Transcrição de tokens"""
    def transc_tokens(my, tokensStatement):
        
        my.transc_stat_comment(tokensStatement)
        print("tokens = (")
        tkns = (tokensStatement)[tokens_key]
        for tkn in tkns:
            print(PTAB + PTAB + tkn + ",")
        print("\t)")


    """Transcrição de literals"""
    def transc_literals(my, literalsStatement):

        my.transc_stat_comment(literalsStatement)
        print("literals = [")
        lits = (literalsStatement)[literals_key]
        for lit in lits:
            print(PTAB + PTAB + "\'" + lit + "\',")
        print("\t]")


    """Transcrição de states"""
    def transc_states(my, statesStatement):

        my.transc_stat_comment(statesStatement)
        print("states = (")
        stats = (statesStatement)[states_key]
        for stat in stats:
            print(PTAB + PTAB + "(" + stat[0] + ", " + stat[1] + "),")
        print("\t)")
    

    """Transcrição de ignore"""
    def transc_ignore(my, ignoreStatement):

        my.transc_stat_comment(ignoreStatement)
        igns = (ignoreStatement)[ignore_key]
        print("ignore = \"" + igns + "\"")

    

    def transc_returns(my, returnStatement):
        
        # cada recStatement é um dicionário
        for retStatement in returnStatement:
            
            my.transc_stat_comment(retStatement)
            varNameQ = (retStatement[return_key])
            # retirar as \' à variável em questão
            varName = (varNameQ)[1:-1]
            if retStatement[states_key] is not None:
                print("def t_" + retStatement[states_key] + "_" + varName + "(t):")
            else:
                print("def t_" + varName + "(t):")
            
            print(PTAB + "r'" + retStatement[regex_key] + "\'")
            if retStatement[varNameQ] != "t.value":
                print(PTAB + "t.value = " + retStatement[varNameQ] + "(t.value)")
            print(PTAB + "return t\n\n")
    

    def transc_error(my, errorStatement=None):

        if errorStatement:
            my.transc_stat_comment(errorStatement)
            errorTuple = errorStatement[error_key]
            print("def t_error(t):")
            print(PTAB + errorTuple[0])
            if len(errorTuple) > 1:
                print(PTAB + errorTuple[1])
            print()
        else:
            print("def t_error(t):")
            print(PTAB + "pass\n")



    def transcribeYacc(my):

        yaccContent = my._yaccObject
        if hasattr(yaccContent, "_hasPrecedence") and yaccContent._hasPrecedence:
            precedence = yaccContent._precedence
            my.transc_precedence(precedence)
        
        productions = yaccContent._productionRules
        my.transc_prodRules(productions)


    def transc_precedence(my, precStatements):

        my.transc_stat_comment(precStatements)
        print("precedence = (")
        precs = (precStatements)[precedence_key]

        for prec in precs:
            for i in range (len(prec)):       #Enquanto houver elementos

                if isinstance(prec[i], str):   #Se for uma string
                    print("\t(" + prec[i] + ',', end="")
                else:
                    for e in range (len(prec[i])):    #Caso seja uma lista

                        if(e == len(prec[i])-1):
                            print(prec[i][e] + "),")
                        else:
                            print(prec[i][e] + ",", end="")
                        e = e + 1
                i = i+1
        print(")\n")


    def transc_prodRule(my, prodStatements, id):
        rule = prodStatements['productionRule']
        print("def p_" + rule + str(id) + "(t):")
        print("\t\"" + rule + " : " + prodStatements[rule] + "\"")
        print("\t" + prodStatements['pythonCode'] + "\n")


    """Transcreve código python - não há necessidade de tratamento extra"""
    def transc_pythonCode(my, pythonCode):
        print(pythonCode)


    """Transcreve plySimple para PLY, conforma a ordem explicitada no ficheiro plySimple"""
    def transcribe_lex_sorted(my):

        hasError = my._lexObject._hasError
        hasIgnore = my._lexObject._hasIgnore
        sortedKeys = my._lexObject._keysOrder
        if hasIgnore is False:
            print("\n#> Warning: ignore rule not defined...")
        if hasError not in sortedKeys:
            print("\n#> Warning: error rule not defined...")

        id = 1
        returnTranscribed = False
        for key in sortedKeys:

            if key == literals_key:
                if my._lexObject._literals[id_key] == id:
                    my.transc_literals(my._lexObject._literals)
                    id = id + 1

            elif key == states_key:
                if my._lexObject._states[id_key] == id:
                    my.transc_states(my._lexObject._states)
                    id = id + 1

            elif key == ignore_key:
                if my._lexObject._ignore[id_key] == id:
                    my.transc_ignore(my._lexObject._ignore)
                    id = id + 1
            
            elif key == error_key:
                if my._lexObject._error[id_key] == id:
                    my.transc_error(my._lexObject._error)
                    id = id + 1

            elif key == tokens_key:
                if my._lexObject._tokens[id_key] == id:
                    my.transc_tokens(my._lexObject._tokens)
                    id = id + 1
            
            elif key == return_key:
                if not returnTranscribed:
                    my.transc_returns(my._lexObject._returns)
                    id = id + len(my._lexObject._returns)
                    returnTranscribed = True
            
            elif key == comment_key:
                for c in my._lexObject._comments:
                    if c[id_key] == id:
                        my.transc_comment(c)
    
            elif key == python_key:
                for p in my._lexObject._pythonCode:
                    if p[id_key] == id:
                        my.transc_python(p)

        # mesmo que não esteja definido, deve ser adicionado
        if hasError is False:
            my.transc_error()


    def transcribe_yacc_sorted(my):

        sortedKeys = my._yaccObject._keysOrder
        id = 1
        ruleNumber = 0
        for key in sortedKeys:

            if key == precedence_key:
                if my._yaccObject._precedence[id_key] == id:
                    my.transc_precedence(my._yaccObject._precedence)
                    id = id + 1
            
            elif key == prodRule_key:
                for prod in my._yaccObject._productionRules:
                    if prod[id_key] == id:
                        my.transc_prodRule(prod, ruleNumber)
                ruleNumber = ruleNumber + 1
                id = id + 1
            
            elif key == comment_key:
                for c in my._yaccObject._comments:
                    if c[id_key] == id:
                        my.transc_comment(c)
            
            elif key == python_key:
                for p in my._lexObject._pythonCode:
                    if p[id_key] == id:
                        my.transc_python(p)
            
    
    def transcribe_plySimple(my):
        my.transcribe_lex_sorted()
        my.transcribe_yacc_sorted()