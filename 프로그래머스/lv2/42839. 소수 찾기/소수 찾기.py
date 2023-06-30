from itertools import permutations
def solution(numbers):
    arr = list(numbers)
    a =[]
    answer = 0
    for i in range(1,len(arr)+1):
        k = list(permutations(numbers, i))
        for j in k:
            num = int(''.join(j))
            if num not in a:
                a.append(num)
    print(a)
    for i in a:
        if is_prime_num(int(i)) == True:
            answer += 1
    return answer

def is_prime_num(k):
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


          