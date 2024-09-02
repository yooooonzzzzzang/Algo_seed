n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1],x[2],x[3]), reverse = True)

idx = 0
# 인덱스 저장
for i in range(n):
    if arr[i][0] == k:
       idx = i
# 등수출력, 같은 등수 체크
for i in range(n):
    if arr[i][1:] == arr[idx][1:]:
        print(i+1)
        break
        