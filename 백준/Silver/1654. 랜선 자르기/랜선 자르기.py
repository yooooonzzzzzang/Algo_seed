k, n = map(int, input().split())
# k <= n
karr = []
for _ in range(k):
    karr.append(int(input()))
start, end = 1, max(karr)
# n개 이상인 mid 가 최대인걸로
# ㅏ <= 10000
while start <= end:
    mid = (start + end) // 2
    if sum( i // mid  for i in karr ) < n:
        end = mid -1
    else:
        start = mid + 1
print(end)
