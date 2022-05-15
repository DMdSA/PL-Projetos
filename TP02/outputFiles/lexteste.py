import sys
sys.path.append('../')
from src.ply import lex
from src.ply import yacc

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

def t_error(t):
	pass

ts = { }
def p_stat0(t):
	"stat : VAR '=' exp"
	ts[t[1]] = t[3] 

def p_stat1(t):
	"stat : exp"
	print(t[1]) 

def p_exp2(t):
	"exp : exp '+' exp"
	t[0] = t[1] + t[3] 

def p_exp3(t):
	"exp : exp '-' exp"
	t[0] = t[1] - t[3] 

def p_exp4(t):
	"exp : exp '*' exp"
	t[0] = t[1] * t[3] 

def p_exp5(t):
	"exp : exp '/' exp"
	t[0] = t[1] / t[3] 

def p_exp6(t):
	"exp : '-' exp %prec UMINUS"
	t[0] = -t[2] 

def p_exp7(t):
	"exp : '(' exp"
	t[0] = t[2] 

def p_exp8(t):
	"exp : NUMBER"
	t[0] = t[1] 

def p_exp9(t):
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
lexer = lex.lex()
y=yacc.yacc()
y.parse("3+4*7")