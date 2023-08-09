def solution(nums):
    answer = 0
    set_len = len(set(nums))
    k = len(nums)//2
    if set_len>k:
        return k
    return set_len