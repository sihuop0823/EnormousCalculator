import re

expression = input().replace(" ", "")

exStack = []
parenthesisStack = []

n = ""
op = "+"

if re.search(r'[가-힣a-zA-Z]', expression):
    print("연산할 수 없는 문자가 포함되어 있음")
    exit()

def apply(stack, op, n):
    if op == "+":
        stack.append(n)
    elif op == "-":
        stack.append(-n)
    elif op == "*":
        stack.append(stack.pop() * n)
    elif op == "/":
        stack.append(stack.pop() / n)


for ch in expression:
    if ch.isdigit():
        n += ch

    elif ch in "+-*/":
        if n == "":
            print("잘못된 수식입니다")
            exit()

        apply(exStack, op, int(n))
        n = ""
        op = ch

    elif ch == "(":
        parenthesisStack.append((exStack, op))
        exStack = []
        op = "+"
        n = ""

    elif ch == ")":
        if n == "":
            print("잘못된 수식입니다")
            exit()

        apply(exStack, op, int(n))

        result = sum(exStack)

        exStack, op = parenthesisStack.pop()
        n = str(result)

if n != "":
    apply(exStack, op, int(n))

print(sum(exStack))


'''
1. 처음에 문자열(한글, 영어) 들어가 있는지 검사

2. 글자 한글자씩 돌면서 숫자면 num에 붙임

3. 연산자 만나면 이전 연산자에 따라 계산

4. * / 면 스택에 가장 최근에 들어온 애랑 먼저 계산

5. 마지막 숫자 처리하고 스택에 있는 거 전부 더해서 계산
'''


