tmp = []
def permutations(arr,numbers,length,v):
    if len(arr) == length:
        tmp.append(arr[:])
        return
    for i in range(len(numbers)):
        if not v[i]:
            v[i] = True
            arr.append(numbers[i])
    
            permutations(arr, numbers, length, v)
    
            v[i] = False
            arr.pop()


def solution(numbers):
    answer = 0
    n = len(numbers)
    nums = set()
    # 순열 
    for i in range(1, n+1):
        v = [0] * len(numbers)
        permutations([],numbers, i, v)
    # [] -> int, set
    for i in range(len(tmp)):
        nums.add(int(''.join(tmp[i])))
        
    # 2. 소수 판별
    for i in nums:
        if is_prime(i):
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
