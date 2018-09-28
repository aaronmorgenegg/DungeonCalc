from version2_python.calculator.dice import *


def testDice(faces, iterations):
    dice = Dice(faces)
    counts = [0]*faces
    print("Testing distribution of a {} after {} rolls".format(dice, iterations))
    for i in range(iterations):
        value = dice.roll() - 1
        counts[value] += 1

    print("# of rolls for each value       : {}".format(counts))
    print("Biggest Difference in     rolls : {}".format(max(counts)-min(counts)))
    for i in range(faces):
        counts[i] = counts[i]/iterations
    print("Average # of rolls              : {}".format(counts))
    print("Biggest Difference in avg rolls : {}".format(max(counts)-min(counts)))
    print()


testDice(4, 40000)
testDice(8, 80000)
testDice(10, 100000)
testDice(12, 120000)
testDice(20, 200000)
testDice(100, 1000000)
