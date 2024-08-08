n = int(input())
tmp = 1
for i in range(1,100000):
    if tmp < n:
        tmp += 6* i
    else:
        print(i)
        break