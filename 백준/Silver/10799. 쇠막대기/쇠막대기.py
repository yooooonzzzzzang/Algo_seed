sticks = list(map(str, input()))
# ()(((()())(())()))(())
'''
1. ( 이면 push
2. ) 면 앞의 값이 ( 면 레이저 '()'-> answer 에 현재 스택의 길이만큼 더한다
3. ) 앞에 값이 ) 면 막대기 '))'answer += 1
'''
stack = []
answer = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if sticks[i-1] == '(':    # 레이저
            answer += len(stack)

        elif sticks[i-1] == ')':  # 막대기
            answer += 1
print(answer)

