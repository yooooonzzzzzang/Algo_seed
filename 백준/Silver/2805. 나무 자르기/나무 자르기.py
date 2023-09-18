n, m = map(int,input().split())
trees = sorted(list(map(int, input().split())))

'''
4 7
20 15 10 17
'''
start = 1
end = sum(trees)
while start <= end:
    mid = (start + end) // 2
    cut = sum(i - mid for i in trees if i > mid)

    # 자른게 더 많다 == cut 이 너무 낮다 == mid 를 높여야한다
    if cut >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)