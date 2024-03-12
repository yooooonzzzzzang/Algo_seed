def solution(numbers):
    # 순열
    def permutation(arr, length):
        if len(arr) == length:
            candidates.add(int(''.join(arr)))
            return
        else:
            for i in range(len(numbers)):
                if v[i] == 0:
                    v[i] = 1
                    arr.append(numbers[i])
                    permutation(arr, length)
                    v[i] = 0
                    arr.pop()
    # 소수 
    def is_prime(k):
        if k < 2:
            return False
        if k==2:
            return True
        if k % 2 == 0:
            return False
        for i in range(3, int(k**0.5)+1, 2):
            if k % i ==0:
                return False
        return True
    answer = 0
    numbers =  [n for n in numbers]
    candidates  = set()
    for i in range(1,len(numbers)+1):
        v  = [0] * len(numbers)
        permutation([], i)
    for i in candidates:
        if is_prime(i):
            answer += 1
    return answer