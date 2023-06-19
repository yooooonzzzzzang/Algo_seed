def solution(num, total):
    answer = []
    hap = 0
    for i in range(num):
        hap += i
    n = (total - hap)//num 
    print(n)
    for i in range(num):
        answer.append(n + i)
    return answer