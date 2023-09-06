

def is_prime(n):
    if n == 1:
        return False
    if n==2 or n==3:
        return True
    if n % 2 == 0:
        return False
    for m in range(3,int(n**0.5)+1):
        if n%m==0:
            return False
    return True
    
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer += 1
    return answer