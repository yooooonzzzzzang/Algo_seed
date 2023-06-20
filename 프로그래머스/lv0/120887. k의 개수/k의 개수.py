def solution(i, j, k):
    answer = 0
    for nums in range(i,j+1):
        strnums = str(nums)
        for num in strnums:
            if num == str(k):
                answer +=1
    return answer