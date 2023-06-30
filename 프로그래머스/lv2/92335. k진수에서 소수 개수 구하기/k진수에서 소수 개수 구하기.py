def jinsu(n,k):
    s =""
    while n > 0:
        s += str(n % k) 
        n = n // k
    return s[::-1]
def is_prime(k):
    if k<2:
        return False
    else:
        if k ==2 or k ==3:
            return True
        for i in range(3, int(k**0.5)+1, 2):
            if k % i == 0:
                return False
    return True

def solution(n, k):
    answer = 0
    str = jinsu(n,k)
    print(str)
    arr = str.split("0")
    for i in arr:
        if i and is_prime(int(i)):
            answer += 1
    return answer