def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    n = len(A)
    for i in range(n):
        popA = A.pop()
        if popA < B[-1]:
            answer += 1
            B.pop()
        else:
            B.pop(0)
            
    return answer