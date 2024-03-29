"""plySimpleLex.py: classe que arrecadará com toda a informação proveniente do PLY-SIMPLE::LEX"""

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

## common keys
lineno_key = "lineno"
comment_key = "comment"
id_key = "id"
python_key = "pythonCode"

class PlySLexObject:

    def __init__(my):
        
        my._idCounter = 1                               ## statement id

        my._hasLiterals = False                         ## flag control for literals definition
        my._hasTokens = False                           ## flag control for tokens definition
        my._hasIgnore = False                           ## flag control for ignore definition
        my._hasError = False
        my._hasStates = False

        my._literals = {}
        my._tokens = {}
        my._ignore = {}
        my._error = {}
        my._returns = []
        my._states = {}
        my._comments = []

        my._pythonCode = []
        my._keysOrder = []

    def reset(my):
        my._idCounter = 1                               ## statement id
        my._hasLiterals = False                         ## flag control for literals definition
        my._hasTokens = False                           ## flag control for tokens definition
        my._hasIgnore = False                           ## flag control for ignore definition
        my._hasError = False
        my._hasStates = False
        my._literals = {}
        my._tokens = {}
        my._ignore = {}
        my._error = {}
        my._returns = []
        my._states = {}
        my._comments = []
        my._pythonCode = []
        my._keysOrder = []
    ##--------------------------------------------------
    ##----------------- Variables gets/sets/deleters ---
    ##--------------------------------------------------
    
    ## literals
    @property
    def literals(my):
        return my._literals
    
    @literals.setter
    def literals(my, value):
        my._literals = value
    
    @literals.deleter
    def literals(my):
        del my._literals

    ## varsFullyDefined
    @property
    def varsFullyDefined(my):
        return my._varsFullyDefined
    
    @varsFullyDefined.setter
    def varsFullyDefined(my, value):
        my._varsFullyDefined = value
    
    @varsFullyDefined.deleter
    def varsFullyDefined(my):
        del my._varsFullyDefined


    ## hasError
    @property
    def hasError(my):
        return my._hasError
    
    @hasError.setter
    def hasError(my, value):
        my._hasError = value
    
    @hasError.deleter
    def hasError(my):
        del my._hasError

    ## hasIgnore
    @property
    def hasIgnore(my):
        return my._hasIgnore
    
    @hasIgnore.setter
    def hasIgnore(my, value):
        my._hasIgnore = value
    
    @hasIgnore.deleter
    def hasIgnore(my):
        del my._hasIgnore


    ## hasTokens
    @property
    def hasTokens(my):
        return my._hasTokens
    
    @hasTokens.setter
    def hasTokens(my, value):
        my._hasTokens = value
    
    @hasTokens.deleter
    def hasTokens(my):
        del my._hasTokens


    ## hasLiterals
    @property
    def hasLiterals(my):
        return my._hasLiterals
    
    @hasLiterals.setter
    def hasLiterals(my, value):
        my._hasLiterals = value
    
    @hasLiterals.deleter
    def hasLiterals(my):
        del my._hasLiterals

    ## idCounter
    @property
    def idCounter(my):
        return my._idCounter
    
    @idCounter.setter
    def idCounter(my, value):
        my._idCounter = value
    
    @idCounter.deleter
    def idCounter(my):
        del my._idCounter
    
    """Incrementar o valor do ID do ticket atual do objeto"""
    def idCounter_inc(my):
        my._idCounter = my._idCounter + 1

    ## literals
    @property
    def literals(my):
        return my._literals

    @literals.setter
    def literals(my, value):
        my._literals = value

    @literals.deleter
    def literals(my):
        del my._literals


    ## tokens
    @property
    def tokens(my):
        return my._tokens

    @tokens.setter
    def tokens(my, value):
        my._tokens = value

    @tokens.deleter
    def tokens(my):
        del my._tokens


    ##--------------------------------------------------
    ##----------------- PLYSIMPLELEX FUNCTIONS ---------
    ##--------------------------------------------------

    """Adiciona os literals"""
    def addLiterals(my, lit):

        if literals_key in lit.keys():

            line = lit[lineno_key]

            if my._hasLiterals is False:
                lit[id_key] = my._idCounter
                my.idCounter_inc()
                my._hasLiterals = True
                my._literals = lit
            else :
                sys.exit("\n#> duplicate reference of \'literals\' lineno: " + str(line))
        else:
            sys.exit("\n#> what you tried to add is not a \'literals\' statement! lineno: " + str(line))

    """Adiciona as tokens"""
    def addTokens(my, tokens):

        if tokens_key in tokens.keys():

            if my._hasTokens is False:
                #tks = {p[2] : p[5], lineno_key : my._tokenizer.lexer.lineno, comment_key : p[8]}
                # campo extra em que, para cada token, confirma se já foi definido ou não
                tokens[definedToken_key] = {}
                eachToken = tokens[definedToken_key]
                for s in tokens[tokens_key]:
                    eachToken[s] = False
                tokens[id_key] = my._idCounter
                my.idCounter_inc()
                my._tokens = tokens
                my._hasTokens = True

            else :
                sys.exit("\n#> duplicate reference of \'tokens\'")
        else:
            sys.exit("\n#> what you tried to add is not a \'tokens\' statement!")

    """Adiciona Definição de tokens"""
    def addTokenDefinition(my, variable):

        # se for um valor de retorno
        if return_key in variable.keys():
            
            # get da variável a retornar
            varToReturn = variable[return_key]
            # se estiver a ser especificado ANTES de ser definido - erro
            if my._hasTokens is False:
                # se os tokens ainda não tiverem sido definidos
                sys.exit("""\n#> unknown reference to \'{}\'
                        Have you defined token's list?""".format(varToReturn))

            # se estiver a ser especificado APOS ser definido
            else:
                
                # get do dicionário de variaveis adicionadas no %tokens =
                varsDict = my._tokens[definedToken_key]
                # se a variável que estamos a especificar já estava completa - erro
                if varsDict[varToReturn] is True:
                    sys.exit("\n#> error! duplicate reference to \'{}'s definition/return value".format(varToReturn))
                # se for a primeira vez que está a ser especificada, atualizar e adicionar
                else:
                    state = variable[states_key]
                    if state is not None and state != "ANY":
                        validState = False
                        states = my._states[states_key]
                        for st in states:
                            s = (st[0])[1:-1]
                            if state == s:
                                validState = True
                                break
                        if validState is False:
                            sys.exit("\n#> error! unknown reference to state : " + str(state) + ", lineno: " + str(variable[lineno_key]))

                    variable[id_key] = my._idCounter
                    my.idCounter_inc()
                    my._returns.append(variable)
                    varsDict[varToReturn] = True

        else:
            sys.exit("\n#> what you tried to add is not a \'return\' specification!")
    
    """Adiciona ignore"""
    def addIgnore(my, ignore):
        
        if ignore_key in ignore.keys():

            if my._hasIgnore is True:
                sys.exit("\n#> duplicate reference to \'ignore\' statement")
            else:
                ignore[id_key] = my._idCounter
                my.idCounter_inc()
                my._ignore = ignore
                my._hasIgnore = True
        else:
            sys.exit("\n#> what you tried to add is not an \'ignore\' statement!")  
    
    """Adiciona Error"""
    def addError(my, error):
        
        if error_key in error.keys():

            if my._hasError is True:
                sys.exit("\n#> duplicate reference to \'error\' statement")
            else:
                error[id_key] = my._idCounter
                my.idCounter_inc()
                my._error = error
                my._hasError = True
        else:
            sys.exit("\n#> what you tried to add is not an \'error\' statement!")

    """Adiciona States"""
    def addStates(my, states):

        if states_key in states.keys():

            if my._hasStates is True:
                sys.exit("\n#> duplicate reference to \'state\' statement")

            else:
                states[id_key] = my._idCounter
                my.idCounter_inc()
                my._states = states
                my._hasStates = True
        else:
            sys.exit("\n#> what you tried to add is not an \'state\' statement")
    
    """Adiciona Comments"""
    def addComment(my, comment):

        comment[id_key] = my._idCounter
        my.idCounter_inc()
        my._comments.append(comment)

    """Adiciona PythonCode"""
    def addPyhtonCode(my, python):
        python[id_key] = my._idCounter
        my.idCounter_inc()
        my._pythonCode.append(python)

    """Adiciona o statement encontrado a lista correta"""
    def addStatement(my, statement):

        ## TOKENS KEY
        if tokens_key in statement.keys():
            my.addTokens(statement)
            my._keysOrder.append(tokens_key)

        ## RETURN KEY
        elif return_key in statement.keys():
            my.addTokenDefinition(statement)
            my._keysOrder.append(return_key)
        
        ## LITERALS KEY
        elif literals_key in statement.keys():
            my.addLiterals(statement)
            my._keysOrder.append(literals_key)
        
        ## IGNORE KEY
        elif ignore_key in statement.keys():
            my.addIgnore(statement)
            my._keysOrder.append(ignore_key)
        
        ## ERROR KEY
        elif error_key in statement.keys():
            my.addError(statement)
            my._keysOrder.append(error_key)
        
        ## STATE KEY
        elif states_key in statement.keys():
            my.addStates(statement)
            my._keysOrder.append(states_key)

        ## COMMENT KEY
        elif comment_key in statement.keys():
            my.addComment(statement)
            my._keysOrder.append(comment_key)

        ## PYTHON KEY
        elif python_key in statement.keys():
            my.addPyhtonCode(statement)
            my._keysOrder.append(python_key)

        ## UNKNOWN KEY - ERROR
        else:
            sys.exit("\n#> error: unknown statement!! lineno: " + str(statement[lineno_key]))


    
    """Confirma se o LEX do plySimple está completo e pode prosseguir para a configuração do YACC"""
    def isReady(my):

        if my._hasTokens is False: 
            sys.exit("PlySimple-error: tokens are missing!")
            # precisa terminar!
        
        elif my._hasIgnore is False:
            print("#> Warning: ignore characters are missing!")
            # não precisa terminar! 

        if my._hasError is False:
            print("#> Warning: error rule is missing!")             
            # não precisa terminar!
        
        varsDict = my._tokens[definedToken_key]
        for variable in varsDict:
            if varsDict[variable] is False:
                sys.exit("PlySimple-error: rule definition for variable \"" + variable + " is missing!")
                # precisa terminar!
        return True                        


    """Imprime as variáveis que já se encontram guardadas na classe"""
    def printVariables(my):

        for v in vars(my):
            print(v , "->     ", vars(my)[v])
    


        
