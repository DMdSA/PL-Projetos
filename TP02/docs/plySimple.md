# Ply Simple : formato de utilização


### %%Lex
 
- modo `rígido`
- literals, ignore e tokens têm de ficar obrigatoriamente definidos
- cada uma das variáveis anteriores têm de ser referidas com um '%' imediatamente antes:
    1. ex01: %literals = "+-*"
    2. ex02: %tokens = [ 'VAR', 'NUMBER' ]
- atributos de literals e de ignore ficam dentro de parênteses
- tokens ficam guardados dentro de uma lista (parênteses retos) e devem estar delimitados por '\''
- Para listas, é aceitável railing comma e multiline blocks
- Para cada um dos tokens definidos, é necessário haver uma definição da regex que o define, assim como o valor retornado aquando do match da mesma
- valores possíveis no return:
    1. ('VAR'), i.e., nome do token
    2. (t.value), i.e., apenas o valor do match
    3. ('VAR' , t.value), em qualquer ordem
- como extra, para redefinir o valor do "t.value", acrescentamos as seguintes opções:
    1. int(t.value)
    2. float(t.value)
    3. list(t.value)
    4. set(t.value)
    5. como default, será tratado como str(t.value)
- para definir um erro, a regex utilizada é ignorada porque se tratará de um valor qualquer arbitrário. deve ficar definida com as seguintes opções:
    1. error(f"..."), correspondendo a uma string formatada
    2. error(t.lexer.skip(\d+)), correspondendo a um skip no lexer
    3. ambos os anteriores, em qualquer ordem
 

## TRANSIÇÃO PARA 
> quando se intercetar "%%yacc", o estado do parser deve ser alterado para ficar a reconhecer a gramática definida para captar o yacc 

### %%YACC

- modo `rigido`
- pode ter, ou não, precedence
- Se tiver, tem de ser identificado com um '%' imediatamente antes, i.e., "%precedence"
- Os valores alocados ficam dentro de uma lista, aceitando, novamente, trailing comma e multiline block
- cada um dos valores tem o seguinte formato:
    1. ( 'left', '+')
    2. ( 'right', 'UMINUS')
    3. ( 'left', '*', '/', '~')
- O formato de cada precedence token fica delimitado por parênteses curvos;
- cada valor está delimitado por '\''
- o primeiro valor é, obrigatoriamente, um dos seguintes valores: left, right (upper/lower)
- tanto é aceite um token como vários

- Para definição da gramática, deve-se cumprir os seguintes requisitos:
- para identificar o nome da regra de produção:
    1. 'nome : ', respeitando os espaços imediatamente antes e após o ':'
    2. a regra propriamente dita pode ter qualquer formato pretendido (não é aceite multiline block)
    3. para delimitar o código python associado à regra, são utilizados brackets, '{' '}', assumindo-se qualquer coisa entre eles como código (inclui multiline block)


## TRANSIÇÃO PARA
> quando se intercetar "%%" sem qualquer atributo associado, deve-se passar para modo `LIVRE`
 
- este espaço fica reservado para um novo estado que servirá para escrever o código python auxiliar à concretização do ply-simple, como funções/variáveis auxiliares