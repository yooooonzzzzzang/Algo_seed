import heapq
def solution(jobs):
    jobs.sort()
    # 작업을 끝날때 조건 검사, 작업이 시작한 시간
    cnt, last = 0, -1
    # heap
    wait = []
    # 현재시간
    time = jobs[0][0]
    length = len(jobs)
    answer = 0
    # 모든 작업을 끝내면 종료
    while cnt < length:
        for s, t in jobs:
            if last < s <= time:
                # 소요시간을 먼저!
                heapq.heappush(wait, (t, s))
        if len(wait) > 0 :
            last = time
            term,start = heapq.heappop(wait)
            cnt += 1
            time += term
            answer += (time - start)
        else:
            time += 1
            
    return answer//length