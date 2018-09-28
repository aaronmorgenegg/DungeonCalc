
tokens = (
    'NUMBER', 'DICE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'SAVE', 'LOAD',
    'STATUS', 'NOTE', 'HEALTH', 'INITIATIVE', 'ARMOR',
    'NEXTTURN', 'RESET',
    'HELP'
)

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_DICE = r'[dD]'
t_SAVE = r'(s)|(save)'
t_LOAD = r'(l)|(load)'
t_STATUS = r'(ss)|(status)'
t_NOTE = r'(note)'
t_HEALTH = r'(hp)|(health)'
t_INITIATIVE = r'(i)|(init)|(initiative)'
t_ARMOR = r'(a)|(av)|(armor)'
t_NEXTTURN = r'(n)|(next)'
t_RESET = r'(r)|(reset)|(clear)|(new)'
t_HELP = r'(h)|(help)'

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


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
