import re

expression = input().replace(" ", "")

exStack = []
parenthesisStack = []

n = ""
op = "+"
plusminusSign = 1


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
            if ch == "-":
                plusminusSign = -1
                continue
            elif ch == "+":
                plusminusSign = 1
                continue
            print("잘못된 수식입니다")
            exit()

        apply(exStack, op, int(n) * plusminusSign)
        n = ""
        plusminusSign = 1
        op = ch

    elif ch == "(":
        parenthesisStack.append((exStack, op))
        exStack = []
        op = "+"
        plusminusSign = 1
        n = ""

    elif ch == ")":
        if n == "":
            print("어딘가 잘못된 수식입니다")
            exit()

        apply(exStack, op, int(n) * plusminusSign)

        result = sum(exStack)

        exStack, op = parenthesisStack.pop()
        n = str(result)
        plusminusSign = 1

if n != "":
    apply(exStack, op, int(n))

print(sum(exStack))


'''
1. 문자열에 한글, 영어가 있는지 검사

2. 숫자는 n에 붙이고 연산자를 만나면 이전 연산자로 계산

3. *, / 는 바로 계산하고 +, - 는 스택에 저장

4. ( 를 만나면 현재 상태를 저장하고 괄호 안 계산 시작

5. ) 를 만나면 괄호 안 결과를 구해서 괄호 밖 계산에 이어서 사용

6. 마지막 숫자를 처리하고 스택 합계를 출력
'''


