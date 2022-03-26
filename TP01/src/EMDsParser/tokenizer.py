"""tokenizer.py: Definição do tokenizer
"""

from include.ply import lex

def getTokenizer():
    """Define e devolve um tokenizer para capturar os campos de cada registo do dataset
    
        Returns :
            lexer : tokenizer com tokens capazes de capturar os campos dos registos
    """


    tokens = (
        'ID',                       ## id
        'DATE',                     ## date
        'WORD',                     ## name, surname, address, modality
        'NUMBER',                   ## age
        'GENDER',                   ## gender
        'BOOLEAN',                  ## federated, medicalResult
        'EMAIL',                    ## email
    )

    t_ID       = r'[a-z0-9]{24}'
    t_DATE     = r'\d{4}(-\d\d){2}'
    t_WORD     = r'[^\W_0-9a-z]+[^\W_0-9]+'
    t_NUMBER   = r'\b\d+\b'
    t_EMAIL    = r'\w(\w[\.\-]?)*\w@\w[\w\-]*(\.[\w\-]{2,})*'
    t_GENDER   = r'\b(?i:[mf])\b'
    t_BOOLEAN  = r'\b(?i:true|false)\b'

    t_ignore = ', \t\n'             ## caracteres que não implicam tratamento especial

    def t_error(t):
        print("Illegal char: '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()
    return lexer