"""plySimple.py: Definição de uma classe que acarrete com todas as inicializações necessárias à configuração de um objeto LEX"""
# confirmar ^

from plySimpleLex import plySLex

from plyS_LexParser import user_tokens

class plySLexer:

    def __init__(my, filename):

        my._inputFilename = filename
        my._plySLex = plySLex()
    
    ## inputFilename
    @property
    def inputFilename(my):
        return my._inputFilename

    @inputFilename.setter
    def inputFilename(my, value):
        my._inputFilename = value

    @inputFilename.deleter
    def inputFilename(my):
        del my._inputFilename

    
    ## plySLex
    @property
    def plySLex(my):
        return my._plySLex

    @plySLex.setter
    def plySLex(my, value):
        my._plySLex = value

    @plySLex.deleter
    def plySLex(my):
        del my._plySLex

    