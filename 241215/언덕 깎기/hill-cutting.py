# 최대랑 최소를 뽑는다
# 이 차를 17 이내로 하면서 비용을 x * x 계산한다
import sys
n = int(input())
arr = [int(input()) for _ in range(n)]
min_cost = sys.maxsize
for low in range(0,101):
    high = low + 17
    cost = 0

    for h in arr:
        if h < low:
            cost += (low - h) ** 2
        elif h > high:
            cost += (h-high) ** 2
    min_cost = min(cost, min_cost)
print(min_cost)
