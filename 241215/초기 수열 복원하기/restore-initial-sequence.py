n =int(input())
arr = list(map(int,input().split()))
# 맨앞 숫자만 정해주면 됨
for i in range(1,n+1):
    tmp = [i]
    now = 0
    for j in range(len(arr)):
        if arr[j]-tmp[-1] > 0:
            tmp.append(arr[j]-tmp[-1])
        else:
            break
    if len(set(tmp)) == n:
        print(*tmp)
        break