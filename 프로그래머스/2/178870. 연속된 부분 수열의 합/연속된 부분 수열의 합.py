def solution(sequence, k):
    # twopointer k 보다 작으면  right += 1, 크면 left +1 
    left = right = 0
    tmp = sequence[0]
    sequence += [0]
    a, b = 10000000,20000000
    while right < len(sequence)-1:
        if tmp <= k :
            if tmp == k:
                if right- left < b-a:
                    a, b = left, right
            right += 1
            tmp += sequence[right]
        else:
            tmp -= sequence[left]
            left += 1
    return [a, b]