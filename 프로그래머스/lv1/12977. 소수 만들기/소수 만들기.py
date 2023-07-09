from itertools import combinations

def is_prime_num(n):
    if n <2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**1//2),2):
        if n%i == 0:
            return False
    return True
def solution(nums):
    answer = 0 
    arr = [sum(i) for i in list(combinations(nums,3))]
    # 3개 조합
    # 소수 판별
    for n in arr:
        if is_prime_num(n):
            answer+=1
    return answer