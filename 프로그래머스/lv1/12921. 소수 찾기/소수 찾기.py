# def solution(n):
#     answer = 0
#     ch = [0] * (n+1)
#     for i in range(2, n+1):
#         if ch[i] == 0:
#             answer += 1
#             for j in range(i, n+1, i):
#                 ch[j] = 1
#     print(ch)
#     return answer


def is_prime(k):
    if k <2:
        return False
    if k==2 or k == 3:
        return True
    if k % 2 == 0:
        return False
    for i in range(3, int(k**0.5)+1, 2):
        if k % i == 0:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(2,n+1):
        if is_prime(i):
            answer += 1
    return answer