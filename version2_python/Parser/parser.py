from version2_python.Actors.status import Status
from version2_python.Actors.unit import Unit
from version2_python.Dice.dice import rollInitiative
from version2_python.Encounter.encounter import Encounter
from version2_python.Parser.lexer import *
from version2_python.help.help import printHelpMenu

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}

encounter = Encounter()


def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_statement_command(t):
    'statement : command'
    pass


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


# def p_command_save_encounter(t):
#     'command : SAVE'
#     global encounter
#     encounter.file_manager.save(encounter, "latest_encounter")
#
#
# def p_command_save_item(t):
#     'command : SAVE NAME'
#     global encounter
#     data = encounter.lookupName(t[2])
#     encounter.file_manager.save(data, t[2])
#
#
# def p_command_load_encounter(t):
#     'command : LOAD'
#     global encounter
#     encounter.file_manager.load("latest_encounter")
#
# def p_command_load_item(t):
#     'command : LOAD NAME'
#     global encounter
#     data = encounter.file_manager.load(t[2])
#     if isinstance(data, Unit):
#         encounter.addUnit(data)


def p_command_next_turn(t):
    'command : NEXTTURN'
    global encounter
    encounter.nextTurn()
    print(str(encounter))


def p_command_reset(t):
    'command : RESET'
    global encounter
    encounter = Encounter()
    print(str(encounter))


def p_command_help(t):
    'command : HELP'
    printHelpMenu()


def p_command_create_unit(t):
    'command : CREATE unit'
    global encounter
    encounter.addUnit(t[2])
    encounter.sortUnits()
    print(str(encounter))


def p_command_create_multiple_units(t):
    'command : CREATE expression unit'
    global encounter
    unit = t[3]
    num = t[2]
    for i in range(num):
        new_unit = Unit(unit.name + str(i+1),
                initiative=rollInitiative(unit.initiative_mod),
                initiative_mod=unit.initiative_mod,
                hp=unit.hp,
                armor=unit.armor,
                note=unit.note,
                status=unit.status)
        encounter.addUnit(new_unit)

    encounter.sortUnits()
    print(str(encounter))


def p_command_delete_unit(t):
    'command : DELETE NAME'
    global encounter
    encounter.deleteUnit(t[2])
    print(str(encounter))


def p_unit(t):
    '''unit : NAME expression'''
    unit = Unit(t[1],
                initiative=rollInitiative(t[2]),
                initiative_mod=t[2],
                hp=0,
                armor=0,
                note="",
                status=[])
    t[0] = unit


def p_unit_hp(t):
    '''unit : unit HEALTH expression'''
    unit = Unit(t[1].name,
                initiative=t[1].initiative,
                initiative_mod=t[1].initiative_mod,
                hp=t[3],
                armor=t[1].armor,
                note=t[1].note,
                status=t[1].status)
    t[0] = unit


def p_unit_armor(t):
    '''unit : unit ARMOR expression'''
    unit = Unit(t[1].name,
                initiative=t[1].initiative,
                initiative_mod=t[1].initiative_mod,
                hp=t[1].hp,
                armor=t[3],
                note=t[1].note,
                status=t[1].status)
    t[0] = unit


def p_unit_status(t):
    '''unit : unit STATUS status'''
    unit = Unit(t[1].name,
                initiative=t[1].initiative,
                initiative_mod=t[1].initiative_mod,
                hp=t[1].hp,
                armor=t[1].armor,
                note=t[1].note,
                status=[t[3]])
    t[0] = unit


def p_unit_note(t):
    '''unit : unit NOTE NAME'''
    unit = Unit(t[1].name,
                initiative=t[1].initiative,
                initiative_mod=t[1].initiative_mod,
                hp=t[1].hp,
                armor=t[1].armor,
                note=t[3],
                status=t[1].status)
    t[0] = unit


def p_status(t):
    '''status : NAME expression'''
    t[0] = Status(t[1], time_total=t[2])


def p_command_edit_armor(t):
    '''command : NAME ARMOR expression'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.armor = t[3]
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_command_edit_health(t):
    '''command : NAME HEALTH expression'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.hp = t[3]
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_command_edit_initiative(t):
    '''command : NAME INITIATIVE expression'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.initiative_mod = t[3]
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_command_edit_note(t):
    '''command : NAME NOTE NAME'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.note = t[3]
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_command_add_status(t):
    '''command : NAME STATUS status'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.status.append(t[3])
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_command_rm_status(t):
    '''command : NAME DELETE STATUS NAME'''
    global encounter
    try:
        unit = encounter.lookupName(t[1])
        unit.removeStatus(t[4])
    except Exception:
        print("Error looking up name {}".format(t[1]))
    print(str(encounter))


def p_error(t):
    print("Syntax error at '%s'" % t)


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

