def solution(k, tangerine):
    answer = 0
    m = max(tangerine)
    cnt_arr = [0] * int(m+1)
    for i in range(len(tangerine)):
        cnt_arr[tangerine[i]] += 1
    cnt_arr.sort(reverse=True)
    for i in range(len(cnt_arr)):
        if k <= 0:
            return answer
        k = k - cnt_arr[i]
        answer += 1