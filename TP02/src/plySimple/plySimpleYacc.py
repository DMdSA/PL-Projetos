"""plyS_YaccObject.py: Classe que arrecadará com toda a informação proveninente do PLY-SIMPLE::YACC."""

from plySimpleObject import precedence_key

class PlySYaccObject:

    def __init__(my):

        my._idCounter = 1
        my._yaccStatements = []

        my._hasPrecedence = False
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


     ## yaccStatements
    @property
    def yaccStatements(my):
        return my._yaccStatements
    
    @yaccStatements.setter
    def yaccStatements(my, value):
        my._yaccStatements = value
    
    @yaccStatements.deleter
    def yaccStatements(my):
        del my._yaccStatements



    """Ao adicionar novos parâmetros de ply, assegura que são únicos e não há repetições"""
    def confirmNewVariable(my, newVariable):
        if precedence_key in newVariable.keys() and my._hasPrecedence is False:
            my._hasPrecedence = True
            return True
        elif precedence_key in newVariable.keys():
            return False
        
        
        return True


    """Preencher este objeto com ID comparável associado a cada nova variável"""
    def addVariable(my, newVariable):
        
        ## Se for a primeira vez que se adiciona um precedence:
        if my.confirmNewVariable(newVariable):
            newVariable["id"] = my.idCounter
            my.idCounter_inc()
            my._yaccStatements.append(newVariable)

        ## Se houver registos duplicados, avisar do erro!
        else:
            raise Exception(f"Duplicated Yacc statement!")




    """Imprime as variáveis que já se encontram guardadas na classe"""
    def printVariables(my):

        for var in my._yaccStatements:
            print(str(var))


