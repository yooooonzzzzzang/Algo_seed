from collections import deque 
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * (bridge_length))
    truck_weights = deque(truck_weights)
    now_weight = 0
    while truck_weights:
        time += 1
        now_weight -= bridge.popleft()
        
        if now_weight + truck_weights[0] <= weight:
            w = truck_weights.popleft()
        else:
            w = 0
        now_weight += w
        bridge.append(w)
          
                
            
    return time + len(bridge)