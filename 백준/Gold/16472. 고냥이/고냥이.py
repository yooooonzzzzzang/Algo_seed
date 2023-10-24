
n = int(input())
arr = list(input())

ans = start = 0
dic = {}
for end in range(len(arr)):
    dic.setdefault(arr[end], 0)
    dic[arr[end]] += 1
    while len(dic) > n: 
        dic[arr[start]] -=1
        if dic[arr[start]] == 0:
            del dic[arr[start]]
        start+=1
    ans = max(ans, end-start+1)
print(ans)