
def partition(arr, low, high):
    # 피벗을 선택 (여기서는 가장 오른쪽 원소를 피벗으로 사용)
    pivot = arr[high]
    i = low - 1  # 작은 원소들의 끝 지점 인덱스 초기화
    for j in range(low, high):  # low부터 high - 1까지 반복
        if arr[j] < pivot:  # 현재 원소가 피벗보다 작다면
            i += 1  # 작은 원소들의 끝 지점을 하나 증가
            arr[i], arr[j] = arr[j], arr[i]  # 원소 교환

    # 피벗을 올바른 위치로 이동
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 피벗의 최종 위치 반환
def quick_sort(arr, low, high):
    if low < high:
        # 파티션 함수 호출
        pi = partition(arr, low, high)

        # 파티션 기준으로 분할하여 정렬
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# 테스트
n = int(input())
arr = list(map(int,input().split()))
quick_sort(arr, 0, n - 1)
print(*arr)