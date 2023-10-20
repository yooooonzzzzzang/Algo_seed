n = int(input())
cnt = 0
while n >= 0:
    # 0 % n , 0 // n 이 되는 걸 몰랐다
    # n // 0 이 division by zero error
    if n % 5 == 0:
        cnt += (n // 5)
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)