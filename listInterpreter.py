def isntFloatStr(num):
    # returns true if the given string is not a float string
    for s in num:
        if (not s.isdigit()) and s != '.' and s != '-':
            return True
    return False

def goodParens(inp):
    # returns true if given string has equal number of open and close parens
    # and has more than zero pairs of parens
    nOpen = -1
    nClose = -1
    for s in inp:
        if s == '(':
            nOpen += 1
        if s == ')':
            nClose += 1
    if nOpen == nClose and nOpen >= 0:
        return True
    else:
        return False

def simplify(inp):
    # recursively evaluates the right-most, inner-most expression
    if inp[0] != '(':
        print(inp)
        return
    idxA = -1
    idxB = -1
    for i,s in enumerate(inp):
        if s == '(':
            idxA = i
    #print(idxA)
    for i,s in enumerate(inp[idxA:]):
        if s == ')':
            idxB = i + idxA
            break
    #print(idxB)
    if idxA == -1 or idxB == -1:
        print("Error: Invalid Command")
        return
    expr = inp[idxA + 1 : idxB]
    #print(expr)
    terms = expr.split(" ")

    if len(terms) != 3:
        print("Error: Invalid Command")
        return
    #print(terms)

    # check if given command matches any built-in functions
    value = False
    if terms[0] == '+':
        if isntFloatStr(terms[1]) or isntFloatStr(terms[2]):
            print("Error: Invalid Command")
            return
        value = float(terms[1]) + float(terms[2])


    elif terms[0] == '-':
        if isntFloatStr(terms[1]) or isntFloatStr(terms[2]):
            print("Error: Invalid Command")
            return
        value = float(terms[1]) - float(terms[2])


    elif terms[0] == '*':
        if isntFloatStr(terms[1]) or isntFloatStr(terms[2]):
            print("Error: Invalid Command")
            return
        value = float(terms[1]) * float(terms[2])


    elif terms[0] == '/':
        if isntFloatStr(terms[1]) or isntFloatStr(terms[2]):
            print("Error: Invalid Command")
            return
        value = float(terms[1]) / float(terms[2])

    # if no functions matched
    if value == False:
        print("Error: Invalid Command")
        return
    newStr = inp[:idxA] + str(value) + inp[idxB+1:]
    #print(newStr)
    # call simplify recursively on simplified string
    simplify(newStr)




def commandLine():
    # takes input from the user and evaluates it
    running = True
    while (running):
        inp = input("> ").strip()

        # exit command
        if inp == "exit":
            running = False
            continue

        if inp == "":
            continue

        # check for invalid inputs

        # command must start with a paren
        """if inp[0] != '(':
            print("Error: Invalid Command")
            continue
            """
        # open paren can't have space after it
        if len(inp) == 1:
            print("Error: Invalid Command")
            continue
        # command must end with close paren
        """if not inp.endswith(')'):
            print("Error: Invalid Command")
            continue
            """
        if not goodParens(inp):
            print("Error: Invalid Command")
            continue

        # run command, simplfies recursively
        else:
            simplify(inp)


commandLine()
