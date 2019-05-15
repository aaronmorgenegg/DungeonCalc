from version2_python.Dice.dice import Dice


reserved = {
    's': 'SAVE',
    'save': 'SAVE',
    'l': 'LOAD',
    'load': 'LOAD',
    'status': 'STATUS',
    'ss': 'STATUS',
    'note': 'NOTE',
    'hp': 'HEALTH',
    'health': 'HEALTH',
    'i': 'INITIATIVE',
    'init': 'INITIATIVE',
    'initiative': 'INITIATIVE',
    'armor': 'ARMOR',
    'av': 'ARMOR',
    'ac': 'ARMOR',
    'a': 'ARMOR',
    'n': 'NEXTTURN',
    'next': 'NEXTTURN',
    'reset': 'RESET',
    'clear': 'RESET',
    'new': 'RESET',
    'r': 'RESET',
    'help': 'HELP',
    'h': 'HELP',
    'add': 'CREATE',
    'create': 'CREATE',
    'mk': 'CREATE',
    'make': 'CREATE',
    'del': 'DELETE',
    'delete': 'DELETE',
    'rm': 'DELETE',
    'remove': 'DELETE',
    'favorite': 'FAVORITE',
    'star': 'FAVORITE',
    'fav': 'FAVORITE',
    'pc': 'FAVORITE',
    'party': 'FAVORITE',
}

tokens = [
    'NUMBER', 'DICE', 'NAME',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
]

for token in set(reserved.values()):
    tokens.append(token)

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


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

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
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
