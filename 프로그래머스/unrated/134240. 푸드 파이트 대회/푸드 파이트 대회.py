def solution(food):
    answer = ''
    len_food = len(food)
    for i in range(1, len_food):
        answer += str(i)*(food[i]//2)
    answer += '0'
    for i in range(1, len_food):
        answer += str(len_food-i)*(food[len_food-i]//2)
    return answer