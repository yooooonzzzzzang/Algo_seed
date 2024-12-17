from collections import deque

def min_time_to_reach_x(X):
    queue = deque([(0, 1, 0)])  # (현재 위치, 현재 속도, 소요 시간)
    visited = set()  # 방문한 상태를 저장 (현재 위치, 현재 속도)
    
    while queue:
        pos, speed, time = queue.popleft()
        
        # 도착 조건: 위치가 X이고 속도가 1일 때
        if pos == X and speed == 1:
            return time
        
        # 이미 방문한 상태인지 체크
        if (pos, speed) in visited:
            continue
        visited.add((pos, speed))
        
        # 다음 상태로 전이
        # 속도를 유지
        if pos + speed <= X + 1:  # 목표 위치를 초과하지 않도록
            queue.append((pos + speed, speed, time + 1))
        
        # 속도를 증가
        if pos + speed + 1 <= X + 1:  # 목표 위치를 초과하지 않도록
            queue.append((pos + speed + 1, speed + 1, time + 1))
        
        # 속도를 감소 (속도가 1보다 클 때만)
        if speed > 1 and pos + speed - 1 <= X + 1:
            queue.append((pos + speed - 1, speed - 1, time + 1))

# 입력 받기
X = int(input())
print(min_time_to_reach_x(X)+1)
