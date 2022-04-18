"""plySimpleLex.py: classe que arrecadará com toda a informação proveniente do PLY-SIMPLE::LEX"""


tokens_key = "tokens"
literals_key = "literals"
ignore_key = "ignore"
error_key = "error"
return_key = "return"
regex_key = "regex"
comment_key = "comment"
lineno_key = "lineno"


class plySLex:

    def __init__(my):

        my._idCounter = 1                               ## statement id
        my._lexerVariables = []                         ## lex statements, each one is a dictionary

        my._hasLiterals = False                         ## flag control for literals definition
        my._hasTokens = False                           ## flag control for tokens definition
        my._hasIgnore = False                           ## flag control for ignore definition
        my._hasError = False                            ## flag control for error definition

        my._varsFullyDefined = {}                       ## flag control for each VAR definition


    ##--------------------------------------------------
    ##----------------- Variables gets/sets/deleters ---
    ##--------------------------------------------------
    

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

    ## lexerVariables
    @property
    def lexerVariables(my):
        return my._lexerVariables

    @lexerVariables.setter
    def lexerVariables(my, value):
        my._lexerVariables = value

    @lexerVariables.deleter
    def lexerVariables(my):
        del my._lexerVariables



    ##--------------------------------------------------
    ##----------------- PLYSIMPLELEX FUNCTIONS ---------
    ##--------------------------------------------------


    """Para cada um dos tokens definidos pelo utilizador, inicializa a sua existência, para posterior definição de regras"""
    def initVariable(my, variable):
        if variable not in my._varsFullyDefined:
            my._varsFullyDefined[variable] = False
            return
        else : raise Exception("Duplicated initialization of var='" + variable + "'!")
    
    """Ao assegurar que o token já foi previamente inicializado, confirma que o utilizador já definiu a regra desse token"""
    def concludeVariable(my, variable):
        if variable in my._varsFullyDefined.keys() and my._varsFullyDefined[variable] is False:
            my._varsFullyDefined[variable] = True
        else : raise Exception("Duplicated definition of return value for var='" + variable + "'!")


    """Ao adicionar novos parâmetros de ply, assegura que são únicos e não há repetições"""
    def confirmNewVariable(my, newVariable):
        
        ## TOKENS KEY
        if tokens_key in newVariable.keys() and my._hasTokens is False:
            for tkn in newVariable[tokens_key]:
                my.initVariable(tkn)
            my._hasTokens = True

        ## RETURN KEY
        elif return_key in newVariable.keys():
            my.concludeVariable(newVariable[return_key])
        
        ## LITERALS KEY
        elif literals_key in newVariable.keys() and my._hasLiterals is False:
            my._hasLiterals = True
        
        ## IGNORE KEY
        elif ignore_key in newVariable.keys() and my._hasIgnore is False:
            my._hasIgnore = True
        
        ## ERROR KEY
        elif error_key in newVariable.keys() and my._hasError is False:
            my._hasIgnore = True
        
        ## DUPLICATED INFO - ERROR
        else:
            raise Exception("Duplicated ply statement! lineno: " + newVariable.lineno_key)
        

    """Preencher este objeto com ID comparável associado a cada nova variável"""
    def addVariable(my, newVariable):
        
        ## Se as variáveis estiverem a ser definidas pela 1ªx no TOKENS:
        my.confirmNewVariable(newVariable)
        newVariable["id"] = my.idCounter
        my.idCounter_inc()
        my._lexerVariables.append(newVariable)
    

    """Verifica se uma VARIAVEL se encontra previamente registada nos tokens da linguagem"""
    def checkTokenExistance(my, variableName):

        for dic in my._lexerVariables:                  ## para cada dicionário dentro da lista de dicionários
            
            if tokens_key in dic.keys():           ## se o dicionário contiver a key:"tokens"
                tokens = dic[tokens_key]           ## retira a lista de tokens
                
                if variableName in tokens:              ## confirma se a variableName faz parte dos tokens pre-definidos
                    return True
                return False
        return False

    """Confirma se o LEX do plySimple está completo e pode prosseguir para a configuração do YACC"""
    def isReady(my):

        if my._hasLiterals is False:
            raise Exception("PlySimple-error: literals are missing!")

        elif my._hasTokens is True: 
            raise Exception("PlySimple-error: tokens are missing!")
        
        elif my._hasIgnore is True:
            raise Exception("PlySimple-error: ignore characters are missing!")          
        
        elif my._hasError is True:
            raise Exception("PlySimple-error: lex error control is missing!")              
        
        else :
            for elem in my._varsFullyDefined:
                if my._varsFullyDefined[elem] is False:
                    raise Exception("PlySimple-error: rule definition for variable \"" + elem + " is missing!")

        return True                        


    """Imprime as variáveis que já se encontram guardadas na classe"""
    def printVariables(my):

        for var in my._lexerVariables:
            print(str(var))
        
    
