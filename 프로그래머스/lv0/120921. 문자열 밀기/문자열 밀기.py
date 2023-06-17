def solution(A, B):
    cnt =0
    origin = list(A)
    if A == B:
        return 0
    for i in range(len(A)):
        k = origin.pop()
        origin.insert(0,k)
        cnt +=1
        if "".join(origin) == B:
            return cnt
    return -1