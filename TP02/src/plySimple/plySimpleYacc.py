"""plyS_YaccObject.py: Classe que arrecadará com toda a informação proveninente do PLY-SIMPLE::YACC."""

import sys

## yacc keys
precedence_key = "precedence"
prodRule_key = "productionRule"

## common keys
lineno_key = "lineno"
comment_key = "comment"
id_key = "id"

class PlySYaccObject:

    def __init__(my):

        my._idCounter = 1
        my._hasPrecedence = False
        my._precedence = {}
        my._productionRules = []
        my._comments = []

        my._keysOrder = []

        # não é preciso mais nada?..
    
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



    def addPrecedence(my, precedence):

        if my._hasPrecedence is False:
            precedence[id_key] = my._idCounter
            my.idCounter_inc()
            my._precedence = precedence
            my._hasPrecedence = True
        
        else:
            sys.exit("\n#> duplicate reference to \'precedence\' statement")


    def addProductionRule(my, rule):

        rule[id_key] = my._idCounter
        my.idCounter_inc()
        my._productionRules.append(rule)


    def addComment(my, comment):

        comment[id_key] = my._idCounter
        my.idCounter_inc()
        my._comments.append(comment)

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
        
        else:
            print(statement)
            sys.exit("\n#> error: unknown statement!! lineno: " + str(statement[lineno_key]))

    """Imprime as variáveis que já se encontram guardadas na classe"""
    def printVariables(my):
        print(vars(my))


