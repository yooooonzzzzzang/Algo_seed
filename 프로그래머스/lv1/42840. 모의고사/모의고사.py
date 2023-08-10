def one(n):
    arr = []
    for i in range(n):
        arr.append(i%5+1)
    return arr

def two(n):
    arr = []
    order = [2,1,2,3,2,4,2,5] 
    for i in range(n):            
        arr.append(order[i%len(order)])
    return arr

def three(n):
    arr = []
    order = [3,3,1,1,2,2,4,4,5,5]
    for i in range(n):            
        arr.append(order[i%len(order)])
    return arr

def correct(answers, arr):
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == arr[i]:
            cnt += 1
    return cnt

def solution(answers):
    ans =[]
    answer = []
    n = len(answers)
    answer.append(correct(answers, one(n)))
    answer.append(correct(answers, two(n)))
    answer.append(correct(answers, three(n)))
    k= max(answer)
    for i in range(3):
        if answer[i] >= k:
            ans.append(i+1)
    return ans