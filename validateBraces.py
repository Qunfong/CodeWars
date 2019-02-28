# Validating braces
# TODO: Fix such that all testcases pass.


def validBraces(string):
    openPar = [x for x in string if x == '(']
    closePar = [x for x in string if x == ')']
    openCur = [x for x in string if x == '{']
    closeCur = [x for x in string if x == '}']
    openBlock = [x for x in string if x == '[']
    closeBlock = [x for x in string if x == ']']

    return (len(openPar) - len(closePar)) + (len(openCur) - len(closeCur)) + (len(openBlock) - len(closeBlock)) == 0


print(validBraces("()"))
