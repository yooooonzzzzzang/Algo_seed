n =int(input())
ppl = list(map(int, input().split()))
tmp = []
for i in range(n-1, -1, -1):
    idx = i
    num = i+1
    order = ppl[i]
    cnt = 0
    if len(tmp)> order:

        for j in range(len(tmp)):
            if cnt == order:
                tmp.insert(j, num)
                break
            if tmp[j] > num:
                cnt +=1


    else:
        tmp.append(num)
print(*tmp)
# 4 2 1 3
# 1 2 3 4 5
# 5 4 3 2 1
# 6 2 3 4 7 5 1
# 6 2 3 4 7 5 1