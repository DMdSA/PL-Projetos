from include.ply import lex
def getTokenizer():
    
    tokens = (
        'ID',
        'DATE',
        'WORD',
        'NUMBER',
        'GENDER',
        'BOOLEAN',
        'EMAIL',
    )

    t_ID       = r'[a-z0-9]{24}'
    t_DATE     = r'\d{4}(-\d\d){2}'
    t_WORD     = r'[^\W_0-9a-z]+[^\W_0-9]+'
    t_NUMBER   = r'\b\d+\b'
    t_EMAIL    = r'\w(\w[\.\-]?)*\w@\w[\w\-]*(\.[\w\-]{2,})*'
    t_GENDER   = r'\b(?i:[mf])\b'
    t_BOOLEAN  = r'\b(?i:true|false)\b'

    t_ignore = ', \t\n'

    def t_error(t):
        print("Illegal char: '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()
    return lexer