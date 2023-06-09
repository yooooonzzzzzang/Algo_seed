
a1 = input()
a2 = list(input())

stack = []

for i in range(len(a1)):
    stack.append(a1[i]) # 스택에 하나씩 추가
    if stack[-len(a2):] == a2: # 스택의 마지막이 m 문자열과 같으면
        del stack[-len(a2):] # 삭제

if stack: print("".join(stack))
else: print("FRULA")