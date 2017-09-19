def findNextOpr(s):
    if len(s)<=0 or not isinstance(s,str):
        print("type mimatch error: findNextOpr")
        return "type mimatch error: findNextOpr"
    
    p = -1
    for (j, i) in enumerate(list(s)):
        if i == '+' or i == '-' or i == '*' or i == '/':
            p = j
            break

    return p
 
 
def isNumber(s):
    if len(s)==0 or not isinstance(s, str):
        print("type mismatch error: isNumber")
        return "type mismatch error: isNumber"

    try:
        float(s.strip())
        return True
    except ValueError:
        return False
 
 
 
def getNextNumber(expr, pos):
    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        print("type mismatch error: getNextNumber")
        return None, None, "type mismatch error: getNextNumber"

    a = findNextOpr(expr[pos:])
    if a == -1:
        a = None
        b = None
        c = expr[pos:]
    elif a == 0:
        pos += 1
        a = findNextOpr(expr[pos:])
        if a == -1:
            a = None
            b = None
            c = expr[pos:]
        else:
            a += pos
            b = expr[a]
            c = "-" + expr[pos:a] 
    else:
        a += pos
        b = expr[a]
        c = expr[pos:a]        

    if not isNumber(c):
        c = None
    else:
        c = float(c)

    return (c, b, a)

 
def exeOpr(num1, opr, num2):
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        return num1/num2
    else:
        return None
 
     
def calc(expr):
    if len(expr)<=0 or not isinstance(expr,str):
        print("argument error: line A in eval_expr")
        return "argument error: line A in eval_expr"
    newNumber, newOpr, oprPos = getNextNumber(expr, 0)
    if newNumber is None:
        print("input formula error: line B in eval_expr")
        return "input formula error: line B in eval_expr"
    elif newOpr is None:
        return newNumber
    elif newOpr=="+" or newOpr=="-":
        mode="add"
        addResult=newNumber
        mulResult=None
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber
    pos=oprPos+1
    opr=newOpr
    while True:
        c, d, e = getNextNumber(expr, pos)
        if d=="+" or d=="-":
            f = "add"
        elif d =="*" or d == "/":
            f = "mul"
        else:
            f = None
        if c is None:
            print("c is None")
            if mode == "add":
                return addResult
            else:
                return mulResult
        
        elif mode == "add" and f == "add":
            addResult = exeOpr(addResult, opr, c)
            return calc(str(addResult) + expr[e:])
        elif mode == "add" and f == "mul":
            if opr == "+":
                return addResult + calc(expr[pos:])
            elif opr == "-":
                return addResult + calc("-" + expr[pos:])
        elif mode == "mul" and f == "mul":
            mulResult = exeOpr(mulResult, opr, c)
            return calc(str(mulResult) + expr[e:])
        elif mode == "mul" and f == "add":
            mulResult = exeOpr(mulResult, opr, c)
            return calc(str(mulResult) + expr[e:])
        elif f == None:
            if mode == "add":
                return exeOpr(addResult, opr, c)
            else:
                return exeOpr(mulResult, opr, c)
        break
