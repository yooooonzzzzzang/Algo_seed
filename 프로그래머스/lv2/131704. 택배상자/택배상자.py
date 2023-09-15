from collections import deque
def solution(order):
    order = deque(order)
    answer = 0
    n = len(order)
    temp = []
    for i in range(1, n+1):
     
        temp.append(i)

        while True:
            if temp and temp[-1] == order[0]:
                temp.pop()
                order.popleft()
                answer += 1
            else:
                break

    return answer