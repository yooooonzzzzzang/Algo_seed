n = int(input())
arr = input()
ans = n # 최대 문자열 길이로 설정
# 문자열 길이
for i in range(1,n+1):
    tmp = set()
    flag = True
    # 시작인데스
    for j in range(n-i+1):
        substrs = arr[j:j+i]

        if substrs in tmp:
            flag = False
            break
        tmp.add(substrs)

    if flag :
        ans = i
        break
print(ans)