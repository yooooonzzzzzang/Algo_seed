def factorical(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp

n, m = map(int, input().split())

print(factorical(n)//(factorical(n-m)*factorical(m)))