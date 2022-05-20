
from encodings import utf_8
from plySimple.plySimpleLex import PlySLexObject
from plySimple.plySimpleYacc import PlySYaccObject
from plySimple.plySimpleParser import PlySimpleParser

## lex keys
from plySimple.plySimpleLex import tokens_key, literals_key, ignore_key, error_key, return_key, regex_key, states_key
## yacc keys (2) + common ones (4)
from plySimple.plySimpleYacc import precedence_key, prodRule_key, comment_key, id_key, python_key


PTAB = '\t'     # python tab

class PlySimple:

    def __init__(self, filename, output):
        
        self._filename = filename
        self._output = output
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

    ## output file
    @property
    def output(my):
        return my._output
    
    @output.setter
    def output(my,value):
        my._output = value
    
    @output.deleter
    def output(my):
        del my._output

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

    """Escreve tudo num ficheiro pela ordem que aparece no ficheiro PlySimple"""
    def transcribe_plySimple(my):

        f = open(my._output, "wt", encoding="utf_8")
        f.write("import sys\nsys.path.append('../')\nfrom src.ply import lex\nfrom src.ply import yacc\n\n")
        my.transcribe_lex_sorted(f)
        my.transcribe_yacc_sorted(f)
        f.close()


    """Transcreve um comentário, caso exista"""
    def transc_stat_comment(my, something,f): 
        if len(something[comment_key]) > 0:
            f.write(something[comment_key] + "\n")

    """Transcrição de comment"""
    def transc_comment(my, comment,f):
        f.write(comment[comment_key] + "\n")


    """Transcrição de tokens"""
    def transc_tokens(my, tokensStatement,f):
        
        my.transc_stat_comment(tokensStatement,f)
        f.write("tokens = (\n")
        tkns = (tokensStatement)[tokens_key]
        for tkn in tkns:
            f.write(PTAB + PTAB + tkn + ",\n")
        f.write("\t)\n\n")


    """Transcrição de literals"""
    def transc_literals(my, literalsStatement,f):

        my.transc_stat_comment(literalsStatement,f)
        f.write("literals = [\n")
        lits = (literalsStatement)[literals_key]
        for lit in lits:
            f.write(PTAB + PTAB + "\'" + lit + "\',\n")
        f.write("\t]\n\n")


    """Transcrição de states"""
    def transc_states(my, statesStatement,f):

        my.transc_stat_comment(statesStatement,f)
        f.write("states = (\n")
        stats = (statesStatement)[states_key]
        for stat in stats:
            f.write(PTAB + PTAB + "(" + stat[0] + ", " + stat[1] + "),\n")
        f.write("\t)\n\n")
    

    """Transcrição de ignore"""
    def transc_ignore(my, ignoreStatement,f):

        my.transc_stat_comment(ignoreStatement,f)
        igns = (ignoreStatement)[ignore_key]
        f.write("ignore = \"" + igns + "\"\n\n")

    
    """Transcrição de returns"""
    def transc_returns(my, returnStatement,f):
        
        # cada recStatement é um dicionário
        for retStatement in returnStatement:
            
            my.transc_stat_comment(retStatement,f)
            varNameQ = (retStatement[return_key])
            # retirar as \' à variável em questão
            varName = (varNameQ)[1:-1]
            if retStatement[states_key] is not None:
                f.write("def t_" + retStatement[states_key] + "_" + varName + "(t):\n")
            else:
                f.write("def t_" + varName + "(t):\n")
            
            f.write(PTAB + "r'" + retStatement[regex_key] + "\'\n")
            if retStatement[varNameQ] != "t.value":
                f.write(PTAB + "t.value = " + retStatement[varNameQ] + "(t.value)\n")
            f.write(PTAB + "return t\n\n")
    
    """Transcrição de erros"""
    def transc_error(my, f, errorStatement=None):

        if errorStatement:
            my.transc_stat_comment(errorStatement,f)
            errorTuple = errorStatement[error_key]
            f.write("def t_error(t):\n")
            f.write(PTAB + errorTuple[0] + "\n")
            if len(errorTuple) > 1:
                f.write(PTAB + errorTuple[1] + "\n\n") 
        else:
            f.write("def t_error(t):\n")
            f.write(PTAB + "pass\n\n")

    """Transcrição de precedentes"""
    def transc_precedence(my, precStatements,f):

        my.transc_stat_comment(precStatements,f)
        f.write("precedence = (\n")
        precs = (precStatements)[precedence_key]
        for prec in precs:
            for i in prec:       #Enquanto houver elementos

                if isinstance(i,str):   #Se for uma string
                    f.write("\t(" + i + ',')
                else:
                    for e in range (len(i)):    #Caso seja uma lista

                        if(e == len(i)-1):
                            f.write(i[e] + "),\n")
                        else:
                            f.write(i[e] + ",")
                        e = e + 1
               
        f.write(")\n\n")

    """Transcrição das Production Rules"""
    def transc_prodRule(my, prodStatements, id,f):
        my.transc_stat_comment(prodStatements,f)
        rule = prodStatements['productionRule']
        f.write("def p_" + rule + str(id) + "(t):\n")
        f.write("\t\"" + rule + " : " + prodStatements[rule] + "\"\n")
        f.write("\t" + prodStatements['pythonCode'] + "\n\n")


    """Transcreve código python - não há necessidade de tratamento extra"""
    def transc_pythonCode(my, pythonCode, f):
        f.write(pythonCode[python_key])
        f.write("\n")


    """Transcreve plySimple para PLY, conforma a ordem explicitada no ficheiro plySimple"""
    def transcribe_lex_sorted(my,f):

        hasError = my._lexObject._hasError
        hasIgnore = my._lexObject._hasIgnore
        sortedKeys = my._lexObject._keysOrder
        my._lexObject.isReady()

        id = 1
        returnTranscribed = False
        for key in sortedKeys:

            if key == literals_key:
                if my._lexObject._literals[id_key] == id:
                    my.transc_literals(my._lexObject._literals,f)
                    id = id + 1

            elif key == states_key:
                if my._lexObject._states[id_key] == id:
                    my.transc_states(my._lexObject._states,f)
                    id = id + 1

            elif key == ignore_key:
                if my._lexObject._ignore[id_key] == id:
                    my.transc_ignore(my._lexObject._ignore,f)
                    id = id + 1
            
            elif key == error_key:
                if my._lexObject._error[id_key] == id:
                    my.transc_error(f, my._lexObject._error)
                    id = id + 1

            elif key == tokens_key:
                if my._lexObject._tokens[id_key] == id:
                    my.transc_tokens(my._lexObject._tokens,f)
                    id = id + 1
            
            elif key == return_key:
                if not returnTranscribed:
                    my.transc_returns(my._lexObject._returns,f)
                    id = id + len(my._lexObject._returns)
                    returnTranscribed = True
            
            elif key == comment_key:
                for c in my._lexObject._comments:
                    if c[id_key] == id:
                        my.transc_comment(c,f)
                        id = id + 1
    
            elif key == python_key:
                for p in my._lexObject._pythonCode:
                    if p[id_key] == id:
                        my.transc_pythonCode(p,f)
                        id = id + 1
        # mesmo que não esteja definido, deve ser adicionado
        if hasError is False:
            my.transc_error(f)

    """Transcreve plySimple para PLY, conforma a ordem explicitada no ficheiro plySimple"""
    def transcribe_yacc_sorted(my,f):

        sortedKeys = my._yaccObject._keysOrder
        id = 1
        ruleNumber = 0
        if sortedKeys:
            my._yaccObject.isReady()

        for key in sortedKeys:

            if key == precedence_key:
                if my._yaccObject._precedence[id_key] == id:
                    my.transc_precedence(my._yaccObject._precedence,f)
                    id = id + 1
            
            elif key == prodRule_key:
                for prod in my._yaccObject._productionRules:
                    if prod[id_key] == id:
                        my.transc_prodRule(prod, ruleNumber,f)
                        id = id + 1
                        ruleNumber = ruleNumber + 1
            
            elif key == comment_key:
                for c in my._yaccObject._comments:
                    if c[id_key] == id:
                        my.transc_comment(c,f)
                        id = id + 1
                    
            
            elif key == python_key:
                for p in my._yaccObject._pythonCode:
                    if p[id_key] == id:
                        my.transc_pythonCode(p,f)
                        id = id + 1
        

