
def solution(N, stages):
    answer = []
    arr = [0] * (N+2)
    for i in range(len(stages)):
        arr[stages[i]] += 1
        
    for i in range(N):
        sums = sum(arr[i+1:])
        if sums == 0:
            answer.append((0, i+1))
        else:
            answer.append((arr[i+1]/sums, i+1))
    answer.sort(reverse=True, key=lambda x: x[0])
    real = []
    for i in answer:
        real.append(i[1])
    return real
