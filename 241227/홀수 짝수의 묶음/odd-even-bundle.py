# 짝수 
# 짝 + 짝 
# 홀 + 홀 
# 짝

# 홀수
# 홀 + 짝 
# 홀 


n = int(input())
arr = list(map(int,input().split()))
odd_cnt = 0
even_cnt = 0
ans = 0 
for i in arr:
    if i % 2 ==0:
        even_cnt += 1
    else:
        odd_cnt += 1
# 짝수만 있을때
if odd_cnt == 0:
    ans = 0
# 홀수만 있을때
elif even_cnt == 0:
    if odd_cnt % 2 == 0:
        ans = odd_cnt // 2 + 1
    else:
        ans = odd_cnt // 2
else:
    # 홀수가 짝수개 있고, 짝수가 짝수개 있을떄
    if odd_cnt %  2== 0 and even_cnt % 2 ==0:
        pass
    # 홀수가 짝수개 있고, 짝수가 홀수개 있을떄
    elif odd_cnt % 2 ==0 and even_cnt % 2 == 1:
        pass
    # 홀수가 홀수개 있고, 짝수가 짝수개 있을떄
    elif odd_cnt % 2 == 1 and even_cnt % 2 == 0:
        pass
     # 홀수가 홀수개 있고, 짝수가 홀수개 있을떄
    else:
        ans += even_cnt
        odd_cnt -= even_cnt
        ans += odd_cnt // 2 + 1
print(ans)
