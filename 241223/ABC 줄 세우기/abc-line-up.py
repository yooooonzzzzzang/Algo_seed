def minimum_swaps_to_sort(arr):
    # 초기화: 스왑 횟수와 배열 길이
    swaps = 0
    
    # 버블 정렬 알고리즘
    for i in range(n):
        for j in range(0, n - i - 1):  # 범위는 점점 줄어듦
            if arr[j] > arr[j + 1]:  # 인접 요소 비교
                # 위치를 바꾸고 스왑 횟수 증가
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    
    return swaps

# 테스트
n = int(input())
initial_order = list(input().split())  # 초기 순서
result = minimum_swaps_to_sort(initial_order)
print(result)

