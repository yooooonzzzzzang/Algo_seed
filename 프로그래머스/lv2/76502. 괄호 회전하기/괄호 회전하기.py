def solution(s):
    answer = 0
    array = []
    for char in s:
        array.append(char)
    for i in range(len(s)):
        # 올바른 문자열인지 확인
        tmp = check(array)
        if tmp :
            answer += 1
        # 돌리기
        k = array.pop(0)
        array.append(k)
    return answer

def check(arr):
    # 스택하나 만들고
    stack = []
    
    for c in arr:
        # 가장 처음엔 상관없이 append
        if not stack:
            stack.append(c)
        # 마지막 스택 같으면 pop
        elif stack[-1] == "{" and c == "}":
            stack.pop()
        elif stack[-1] == "[" and c == "]":
            stack.pop()
        elif stack[-1] == "(" and c == ")":
            stack.pop()
        # 아니면 스택에 저장
        else:
            stack.append(c)
    # 다 끝나고 스택의 길이가 0 이면 올바른 괄호
    if not stack:
        return True
    else: return False