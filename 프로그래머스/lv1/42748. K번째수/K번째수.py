def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        i,j,k = commands[i]
        arr = []
        for index in range(i-1,j):
            arr.append(array[index])
        arr.sort()
        answer.append(arr[k-1])
    return answer