n = int(input())
blocks = list(map(int, input().split()))


even = 0
odd = 0
for block in blocks:
    if(block % 2 == 0):
        even += 1
    else:
        odd += 1
ans = 0 
while True:
    if ans % 2 == 0:
        if even:
            even -= 1
            ans += 1
        elif odd >= 2 :
            odd -= 1
            ans += 1
        else:
            # 그룹을 못만듦 -> 홀수가 0, 1 개 개수 못늘림
            if odd > 0:
                ans -= 1
            break

    else:
        if odd:
            odd -= 1
            ans += 1
        else:
            break
print(ans)