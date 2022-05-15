"""plyS_YaccObject.py: Classe que arrecadará com toda a informação proveninente do PLY-SIMPLE::YACC."""

import sys

## yacc keys
precedence_key = "precedence"
prodRule_key = "productionRule"

## common keys
lineno_key = "lineno"
comment_key = "comment"
id_key = "id"
python_key = "pythonCode"

class PlySYaccObject:

    def __init__(my):

        my._idCounter = 1
        my._hasPrecedence = False
        my._precedence = {}
        my._hasProdRules = False
        my._productionRules = []
        my._comments = []
        my._pythonCode = []
        my._keysOrder = []

    
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

    """Adiciona Precedencias, se houverem duas precendencias dá error"""
    def addPrecedence(my, precedence):

        if my._hasPrecedence is False:
            precedence[id_key] = my._idCounter
            my.idCounter_inc()
            my._precedence = precedence
            my._hasPrecedence = True
        
        else:
            sys.exit("\n#> duplicate reference to \'precedence\' statement")

    """Adiciona uma Regra de Produção"""
    def addProductionRule(my, rule):

        rule[id_key] = my._idCounter
        my.idCounter_inc()
        my._productionRules.append(rule)
        my._hasProdRules = True

    """Adiciona comentários"""
    def addComment(my, comment):

        comment[id_key] = my._idCounter
        my.idCounter_inc()
        my._comments.append(comment)

    """Adiciona código Python"""
    def addPyhtonCode(my, python):
        python[id_key] = my._idCounter
        my.idCounter_inc()
        my._pythonCode.append(python)

    """Adiciona o statement encontrado a lista correta"""
    def addStatement(my, statement):

        ## PRECEDENCE KEY
        if precedence_key in statement.keys():
            my.addPrecedence(statement)
            my._keysOrder.append(precedence_key)
        
        ## RULE KEY
        elif prodRule_key in statement.keys():
            my.addProductionRule(statement)
            my._keysOrder.append(prodRule_key)
        
        elif comment_key in statement.keys():
            my.addComment(statement)
            my._keysOrder.append(comment_key)
        
        elif python_key in statement.keys():
            my.addPyhtonCode(statement)
            my._keysOrder.append(python_key)

        else:
            print(statement)
            sys.exit("\n#> error: unknown statement!! lineno: " + str(statement[lineno_key]))


    """Confirma se o yacc está completo e se pode prosseguir"""
    def isReady(my):
        
        if my._hasProdRules is False: 
            sys.exit("PlySimple-error: Production Rules are missing!") 
        return True       

    """Imprime as variáveis que já se encontram guardadas na classe"""
    def printVariables(my):

        for v in vars(my):
            print(v , "->     ", vars(my)[v])


