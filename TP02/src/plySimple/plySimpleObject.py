
from plySimple.plySimpleLex import PlySLexObject
from plySimple.plySimpleYacc import PlySYaccObject
from plySimple.plySimpleParser import PlySimpleParser
import sys


## lex keys
tokens_key = "tokens"
definedToken_key = "alreadyDefined"
literals_key = "literals"
ignore_key = "ignore"
error_key = "error"
return_key = "return"
regex_key = "regex"
states_key = "states"
## yacc keys
precedence_key = "precedence"
prodRule_key = "productionRule"
## common keys
lineno_key = "lineno"
comment_key = "comment"
id_key = "id"

PTAB = '\t'                                 # python tab

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
                parser._parser.parse(auxString)
                auxString = ""

        fHandler.close()

        print("\n#>\n")
        my._lexObject.printVariables()
        print("\n#>\n")
        my._yaccObject.printVariables()
        print("\n\n\n\n")



    """Transcreve a gramática recolhida da parte do LEX e traduz para python"""
    def transcribeLex(my):

        lexContent = my._lexObject
        if hasattr(lexContent, "_hasTokens") and lexContent._hasTokens:
            tokens = lexContent._tokens
            my.transc_tokens(tokens)

        else:
            sys.exit("\n#> error! tokens have not been defined!")

        if hasattr(lexContent, "_hasLiterals") and lexContent._hasLiterals:
            literals = lexContent._literals
            my.transc_literals(literals)

        if hasattr(lexContent, "_hasStates") and lexContent._hasStates:
            states = lexContent._states
            my.transc_states(states)

        if hasattr(lexContent, "_hasIgnore") and lexContent._hasIgnore:
            ignore = lexContent._ignore
            my.transc_ignore(ignore)
        
        else:
            print("\n#> warning: ignore rule not defined")

        if hasattr(lexContent, "_hasTokens") and lexContent._hasTokens:
            returns = lexContent._returns
            my.transc_returns(returns)
        
        if hasattr(lexContent, "_hasError") and lexContent._hasError:
            error = lexContent._error
            my.transc_error(error)
        
        else:
            print("\n#> warning: error rule not defined")
            my.transc_error()


    """Transcreve um comentário, caso exista"""
    def transc_comment(my, something):
        
        if len(something[comment_key]) > 0:
            print(something[comment_key])


    """Transcrição de tokens"""
    def transc_tokens(my, tokensStatement):
        
        my.transc_comment(tokensStatement)
        print("tokens = (")
        tkns = (tokensStatement)[tokens_key]
        for tkn in tkns:
            print(PTAB + PTAB + tkn + "\",")
        print("\t)")


    """Transcrição de literals"""
    def transc_literals(my, literalsStatement):

        my.transc_comment(literalsStatement)
        print("literals = [")
        lits = (literalsStatement)[literals_key]
        for lit in lits:
            print(PTAB + PTAB + "\'" + lit + "\',")
        print("\t]")


    """Transcrição de states"""
    def transc_states(my, statesStatement):

        my.transc_comment(statesStatement)
        print("states = (")
        stats = (statesStatement)[states_key]
        for stat in stats:
            print(PTAB + PTAB + "(" + stat[0] + ", " + stat[1] + "),")
        print("\t)")
    

    """Transcrição de ignore"""
    def transc_ignore(my, ignoreStatement):

        my.transc_comment(ignoreStatement)
        igns = (ignoreStatement)[ignore_key]
        print("ignore = \"" + igns + "\"")

    

    def transc_returns(my, returnStatement):
        
        # cada recStatement é um dicionário
        for retStatement in returnStatement:
            
            my.transc_comment(retStatement)
            varNameQ = (retStatement[return_key])
            # retirar as \' à variável em questão
            varName = (varNameQ)[1:-1]
            print("def t_" + varName + "(t):")
            print(PTAB + "r'" + retStatement[regex_key] + "\'")
            if retStatement[varNameQ] != "t.value":
                print(PTAB + "t.value = " + retStatement[varNameQ] + "(t.value)")
            print(PTAB + "return t\n\n")
    

    def transc_error(my, errorStatement=None):

        if errorStatement:
            my.transc_comment(errorStatement)
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

        my.transc_comment(precStatements)
        print("precedence = (")
        precs = (precStatements)[precedence_key]

        for prec in precs:
            for i in range (len(prec)):       #Enquanto houver elementos

                if isinstance(prec[i],str):   #Se for uma string
                    print("(" + prec[i] + ',', end="")
                else:
                    for e in range (len(prec[i])):    #Caso seja uma lista

                        if(e == len(prec[i])-1):
                            print(prec[i][e] + "),")
                        else:
                            print(prec[i][e] + ",", end="")
                        e = e + 1
                i = i+1
        print(")")
    
    def transc_prodRules(my, prodStatements):

        
        numberProd = 0
        for prodRule in prodStatements:
            my.transc_comment(prodRule)
            rule = prodRule['productionRule']
            print("def p_" + rule + str(numberProd) + "(p):")
            print("\t\"" + rule + " : " + prodRule[rule] + "\"")
            print("\t" + prodRule['pythonCode'])

            numberProd = numberProd + 1
            print("\n")
