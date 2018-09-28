from version2_python.Parser.lexer import *
from version2_python.Dice.dice import *
from version2_python.runDungeonCalc import encounter

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'DICE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_expr(t):
    'statement : expression'
    print(t[1])


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_dice(t):
    '''expression : DICE NUMBER
                  | NUMBER DICE NUMBER'''
    if len(t) == 4:
        t[0] = Dice(t[3]).roll(t[1])
    else:
        t[0] = Dice(t[2]).roll()


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def startParser():
    lexer = buildLexer()

    import ply.yacc as yacc

    parser = yacc.yacc()

    while True:
        try:
            s = input('Input > ')
        except EOFError:
            break
        parser.parse(s)
