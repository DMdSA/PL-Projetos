
from plySimpleLex import PlySLexObject
from plySimpleYacc import PlySYaccObject



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