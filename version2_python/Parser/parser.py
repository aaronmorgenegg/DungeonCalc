from version2_python.Actors.unit import Unit
from version2_python.Parser.lexer import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
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


def p_expression_dice(t):
    '''expression : DICE'''
    t[0] = t[1]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_command_expression(t):
    'command : expression'
    print(t[1])


def p_command_save_encounter(t):
    'command : SAVE'
    encounter.file_manager.save(encounter, "latest_encounter")


def p_command_save_item(t):
    'command : SAVE NAME'
    data = encounter.lookupName(t[2])
    encounter.file_manager.save(data, t[2])


def p_command_load_encounter(t):
    'command : LOAD'
    global encounter
    encounter = encounter.file_manager.load("latest_encounter")

def p_command_load_item(t):
    'command : LOAD NAME'
    data = encounter.file_manager.load(t[2])
    if isinstance(data, Unit):
        encounter.addUnit(data)


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

