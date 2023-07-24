def solution(s):
    stack = []
    # ( 먼저 들어가야 올바른 괄호
    for i in s:
        if i == ')':
            # ) 부터 시작해서 잘못됨
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
        else:
            stack.append(i)
    if not stack:
        return True
    else: return False
