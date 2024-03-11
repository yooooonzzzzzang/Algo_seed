from collections import deque 
def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([0] * (bridge_length))
    truck_weights = deque(truck_weights)
    # 다리를 건너는 현재 무게
    now_weight = 0
    while truck_weights:
        # 1초마다 다리를 나감 
        time += 1
        now_weight -= bridge.popleft()
        # 추가로 다리에 더 올릴수 있으면
        if now_weight + truck_weights[0] <= weight:
            # 올리고
            t  = truck_weights.popleft()
            now_weight += t
            bridge.append(t)
        else:
            # 안되면 0 을 추가
            bridge.append(0)
    # 시간 + 남은 다리에 있는 차 (개수당 1초)
    return time + len(bridge)