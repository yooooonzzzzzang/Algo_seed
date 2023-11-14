
import math

def solution(arr):
    ans = arr[0]
    for n in arr:
        ans = ans * n // math.gcd(ans, n)
    return ans










