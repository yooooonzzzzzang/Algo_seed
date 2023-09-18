a_len = int(input())
a = sorted(list(map(int, input().split())))
m_len = int(input())
m = list(map(int, input().split()))

for i in range(m_len):
    target = m[i]
    left, right = 0, a_len-1
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        if a[mid] == target:
            answer = 1
            break
        elif a[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    print(answer)