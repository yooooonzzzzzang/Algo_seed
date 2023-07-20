def solution(sizes):
    answer = 0
    max_arr = []
    min_arr = []
    for w, h in sizes:
        max_arr.append(max(w,h))
        min_arr.append(min(w,h))
    print(max_arr)
    print(min_arr)
    return max(max_arr)*max(min_arr)