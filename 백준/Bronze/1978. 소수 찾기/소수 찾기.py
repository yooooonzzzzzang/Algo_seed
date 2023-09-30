def is_prime(n):
    if n < 2:
        return False
    if n ==2 or n== 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n **0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int,input().split()))
answer = 0
for i in range(n):
    if is_prime(nums[i]):
        answer += 1
print(answer)