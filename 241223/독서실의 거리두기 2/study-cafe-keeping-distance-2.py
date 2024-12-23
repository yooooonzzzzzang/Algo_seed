n = int(input())
arr = list(input())
max_v = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1':
            if arr[j] =='1' :
                if j-i > max_v:
                    max_v = j-i
                    max_idx = (i,j)
                break
max_v = 1000
for i in range(1,n):
    if arr[i] == '1':
        max_v = i
        break

for i in range(n-2,-1,-1):
    if arr[i] == '1':
        max_v = max(max_v, n-1-i)
        break

arr[(max_idx[1] + max_idx[0])//2] = '1'

for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1':
            if arr[j] =='1':
                if j-i < max_v:
                    max_v = j-i
                break
print(max_v)

# 맨앞에 1 이거나 맨 뒤에 1인경우의 max 랑 ㅂㅣ교 추가 