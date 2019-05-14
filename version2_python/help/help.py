
def printHelpMenu():
    print("-----HELP-----")
    print("Calculator:")
    print(" Enter any math equation or dice roll to evaluate it.")
    print(" ex. 5+20/4")
    print(" ex. 11d6+4")
    print("Encounters:")
    print("Create units: mk/create/add NAME INIT_MOD")
    print("Ex. mk kobold 1")
    print("Create multiple units: mk/create/add X NAME INIT_MOD")
    print("Ex. mk 5 kobold 1")
    print("Create units with stats: mk/create/add NAME INIT_MOD ?HP/HEALTH expression ?AC/ARMOR expression ?NOTE string ?SS/STATUS NAME EXPRESSION")
    print("Ex. mk kobold 1 hp 1d8+1 ac 17 note leader status hasted 3")
