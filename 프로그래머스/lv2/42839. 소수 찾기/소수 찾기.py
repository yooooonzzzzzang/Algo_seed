from itertools import permutations
def solution(numbers):
    answer = 0
    n = len(numbers)
    nums = set()
    # 1. 1~ n 개 만큼 permutation (n) 개로 순열, set으로 중복제거
    for i in range(1, n+1):
        per_nums = list(permutations(numbers, i))
        for j in range(len(per_nums)):
            nums.add(int(''.join(per_nums[j])))
    # 2. 소수 판별
    for i in nums:
        if is_prime(i) == True:
            answer += 1
    return answer

def is_prime(k):
    if k<2:
        return False
    else:
        if k ==2 or k ==3:
            return True
        if k % 2 ==0:
            return False
        for i in range(3, int(k**0.5)+1, 2):
            if k % i == 0:
                return False
    return True
