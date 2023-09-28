n = int(input())
answer = 0
hints = [list(map(int , input().split())) for _ in range(n)]
    # a, b, c 는 정답 후보들 -> hint 들을 다 부합해야함
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            cnt = 0
            for hint in hints:
                num = str(hint[0])
                strike = hint[1]
                ball = hint[2]
                tmp = str(a) + str(b) + str(c)

                if ( a== b) or (b==c) or (c== a):
                    continue
                ball_cnt = 0
                strike_cnt = 0

                for i in range(3):
                    if num[i] == tmp[i]:
                        strike_cnt += 1
                for i in range(3):
                    if num[i] in tmp and num[i] != tmp[i]:
                        ball_cnt += 1

                if ball == ball_cnt and strike_cnt == strike:
                    cnt += 1
            if cnt == n:
                answer += 1
print(answer)
