expression = input()

exStack = []
res = 0
num = ""
op = "+"

for ch in expression:
    if ch.isdigit():

        num += ch

    else:
        n = int(num)

        if op == "+":
            exStack.append(n)

        elif op == "-":
            exStack.append(-n)
            
        elif op == "*":
            exStack.append(exStack.pop() * n)

        elif op == "/":
            exStack.append(exStack.pop() / n)
        
        # ㅁㅇ러ㅣㄴㅁ런ㄹ 
        # stack에 쌓이면 어 무튼 1 + 2 * 3 이면 1 2 * 3 먼저 계산이니까 2먼저 들어오니까 1 , 6 되고
        # sum으로 더하고 

        op = ch
        num = ""

if num != "":
    n = int(num)

    if op == "+":
        exStack.append(n)

    elif op == "-":
        exStack.append(-n)

    elif op == "*":
        exStack.append(exStack.pop() * n)

    elif op == "/":
        exStack.append(exStack.pop() / n)

print(sum(exStack))