n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]

for i in range(1,10001):
    num = i
    flag = True
    for a, b in arr:
        num *= 2
        if a > num or num > b:
            flag = False
    if flag :
        print(i)
        break

