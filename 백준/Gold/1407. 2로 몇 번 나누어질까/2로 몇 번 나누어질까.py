def solve(n, num):
    for i in range(1,50):
        n += (num//(2**i))*((2**i)-(2**(i-1)))
    return n

a, b = map(int,input().split())
a -= 1
tmp_a = a
tmp_b = b
print(solve(tmp_b, b)-solve(tmp_a, a))
