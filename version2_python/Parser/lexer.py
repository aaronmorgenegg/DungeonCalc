from version2_python.Dice.dice import Dice

tokens = (
    'NUMBER', 'DICE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'SAVE', 'LOAD',
    'NAME', 'STATUS', 'NOTE', 'HEALTH', 'INITIATIVE', 'ARMOR',
    'NEXTTURN', 'RESET',
    'DELETE', 'CREATE',
    'HELP'
)

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_SAVE = r'(save)|(s)'
t_LOAD = r'(load)|(l)'
t_STATUS = r'(status)|(ss)'
t_NOTE = r'(note)'
t_HEALTH = r'(health)|(hp)'
t_INITIATIVE = r'(initiative)|(init)|(i)'
t_ARMOR = r'(armor)|(ac)|(av)|(a)'
t_NEXTTURN = r'(next)|(n)'
t_RESET = r'(reset)|(clear)|(new)|(r)'
t_HELP = r'(help)|(h)'
t_CREATE = r'(add)|(create)|(mk)|(make)'
t_DELETE = r'(del)|(delete)|(rm)|(remove)'

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_DICE(t):
    r'\d*d\d+'
    num = t.value.split("d")[0]
    if num == "": num = "1"
    faces = t.value.split("d")[1]
    dice = Dice(int(faces))
    t.value = dice.roll(int(num))
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
def buildLexer():
    import ply.lex as lex

    lexer = lex.lex()
    return lexer
