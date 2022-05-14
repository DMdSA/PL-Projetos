from ply import lex
from ply import yacc

## a single char
literals = [
		'+',
		'-',
		'/',
		'*',
		'=',
		'(',
		')',
	]

# grande estado
states = (
		('COISO', 'inclusive'),
		('DIOGO', 'exclusive'),
	)

b = "rebelo"
ignore = " \t\n"

tokens = (
		'VAR',
		'NUMBER',
	)

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return t

def t_ANY_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

a = "diogo"

def t_error(t):
	pass

ts = { }
def p_stat0(t):
	"stat : VAR '=' exp"
	ts[t[1]] = t[3] 

def p_stat0(t):
	"stat : exp"
	print(t[1]) 

def p_exp0(t):
	"exp : exp '+' exp"
	t[0] = t[1] + t[3] 

def p_exp0(t):
	"exp : exp '-' exp"
	t[0] = t[1] - t[3] 

def p_exp0(t):
	"exp : exp '*' exp"
	t[0] = t[1] * t[3] 

def p_exp0(t):
	"exp : exp '/' exp"
	t[0] = t[1] / t[3] 

def p_exp0(t):
	"exp : '-' exp %prec UMINUS"
	t[0] = -t[2] 

def p_exp0(t):
	"exp : '(' exp"
	t[0] = t[2] 

def p_exp0(t):
	"exp : NUMBER"
	t[0] = t[1] 

def p_exp0(t):
	"exp : VAR"
	t[0] = getval(t[1]) 

precedence = (
	('left','+','-'),
	('left','*','/'),
	('right','UMINUS'),
)

# symboltable : dictionary of variables
ts = { }
def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")
def getval(n):
    if n not in ts: print(f"Undefined name '{n}'")
    return ts.get(n,0)
y=yacc()
y.parse("3+4*7")
