def solution(nums):
    answer = 0
    need = len(nums)//2
    pocketmon = set(nums)
    return need if len(pocketmon) >= need else len(pocketmon) 
