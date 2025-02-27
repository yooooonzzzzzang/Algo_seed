import heapq 
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    
    while n > 0:
        num = heapq.heappop(works)
        num += 1
        heapq.heappush(works, num)
        n-=1
    return sum(i*i for i in works)