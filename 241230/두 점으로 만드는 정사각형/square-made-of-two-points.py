# 변수 선언 및 입력:
x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

# 주어진 값들 중 가장 큰 x에서 가장 작은 x를 뺀 길이가 
# 세로 길이가 되어야 합니다.
# 마찬가지 이유로 가장 큰 y에서 가장 작은 y를 뺀 길이가
# 가로 길이가 되어야 합니다.
width = max(x2, a2) - min(x1, a1)
height = max(y2, b2) - min(y1, b1)

ans =max(width, height)
print(ans*ans)