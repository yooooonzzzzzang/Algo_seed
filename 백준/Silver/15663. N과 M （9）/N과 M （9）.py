from itertools import permutations
n, m = map(int, input().split())
# 4 4 2

arr = list(map(int,input().split()))
a = list(set(list(permutations(arr, m))))
a.sort()
for i in a:
    for j in range(m):
        print(i[j], end=" ")
    print("")
