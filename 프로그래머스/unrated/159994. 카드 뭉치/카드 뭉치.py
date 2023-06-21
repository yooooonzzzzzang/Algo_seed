def solution(cards1, cards2, goal):
    answer = 'No'
    for i in range(len(goal)):
    
        if cards1 and goal[0] == cards1[0]:
            print("1번")
            goal.pop(0)
            cards1.pop(0)
        elif cards2 and goal[0] == cards2[0]:
            print("2번")
            goal.pop(0)
            cards2.pop(0)
        else:
            break
    if not goal:
        answer = 'Yes'

    return answer



