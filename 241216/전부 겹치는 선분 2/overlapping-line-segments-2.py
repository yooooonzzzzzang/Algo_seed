n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def can_all_overlap(arr, n):
    for k in range(n):  # k번째 선분을 제외
        min_start, max_end = -float('inf'), float('inf')

        # k를 제외한 나머지 선분들로 교집합 확인
        for i in range(n):
            if i == k:
                continue
            min_start = max(min_start, arr[i][0])  # 최대 시작점
            max_end = min(max_end, arr[i][1])    # 최소 종료점
        
        # 교집합이 존재한다면
        if min_start <= max_end:
            return "Yes"
    return "No"

print(can_all_overlap(arr, n))
