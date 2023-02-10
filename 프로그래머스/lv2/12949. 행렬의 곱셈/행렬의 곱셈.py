def solution(arr1, arr2):
    arr1_r = len(arr1)
    arr1_c = len(arr1[0])
    arr2_r = len(arr2)
    arr2_c = len(arr2[0])
    answer = [[] * arr2_c for _ in range(arr1_r)]
    for i in range(arr1_r):
        tmp = [0] * arr2_c
        for j in range(arr1_c):
            for k in range(arr2_c):
                tmp[k] += arr1[i][j] * arr2[j][k]
        answer[i] = tmp
    return answer