def solution(n):
    answer = ''   
    while n > 0:
        remainder = n % 3 
        if remainder == 0:
            n = n//3-1
            remainder = 4
        else:
            n = n//3
        answer += str(remainder)
    
    return answer[::-1]
