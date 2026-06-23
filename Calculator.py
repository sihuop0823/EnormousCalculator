expression = input()

res = 0
num = ""
op = "+"

for ch in expression:
    if ch.isdigit():
        num += ch
    else:
        if num != "":
            if op == "+":
                res += int(num)
            elif op == "-":
                res -= int(num)
            elif op == "*":
                res *= int(num)
            elif op == "/":
                res /= int(num)

        op = ch
        num = ""

if num != "":
    if op == "+":
        res += int(num)
    elif op == "-":
        res -= int(num)
    elif op == "*":
        res *= int(num)
    elif op == "/":
        res /= int(num)
    

print(res)