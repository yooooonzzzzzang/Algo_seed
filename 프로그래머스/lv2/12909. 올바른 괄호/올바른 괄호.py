def solution(s):
    stack = []
    for i in s:
        if i == ')':
            if not stack:
                return False
            stack.pop()
        else :stack.append(i)
    if stack:
        return False
    return True