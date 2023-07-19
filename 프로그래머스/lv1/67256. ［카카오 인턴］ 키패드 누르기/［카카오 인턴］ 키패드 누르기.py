def solution(numbers, hand):
    answer = ''
    # Keypad 0123456789*(10)#(11)
    h = {'left':'L', 'right':'R'}
    distance = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    left, right = 10, 11
    for i in numbers:
        if i in (1,4,7):
            answer += 'L'
            left = i
        elif i in (3,6,9):
            answer += 'R'
            right = i
        else:
            # 현재 키패드와 가까운 엄지손가락 사용 
            right_distance = abs(distance[right][0] - distance[i][0]) + abs(distance[right][1] - distance[i][1])
            left_distance = abs(distance[left][0] - distance[i][0]) + abs(distance[left][1] - distance[i][1])
            
            # 같다면 h[hand]
            if right_distance == left_distance:
                answer += h[hand]
                if hand == 'right':
                    right = i
                else:
                    left = i
            elif right_distance > left_distance:
                answer += 'L'
                left = i
            else:
                answer += 'R'
                right = i
    return answer