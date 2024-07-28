from collections import Counter
def solution(weights):
    answer = 0
    # 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면
    counter = Counter(weights)
    # x = 3/2y , x = 2y , x = 4/3y
    for i in range(100,1001):
        if counter[i] > 0:
                answer += counter[i] * (counter[i] - 1) // 2
                answer += counter[i] * counter[i * 3 / 2]
                answer += counter[i] * counter[i * 2]
                answer += counter[i] * counter[i * 4 / 3]
    return answer