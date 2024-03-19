import heapq
def solution(operations):
    min_heap = []
    for op in operations:
        m, n = op.split(" ")
        n = int(n)
        if m == 'I':
            heapq.heappush(min_heap, n)
        else:
            if min_heap:
                if n > 0:
                    # 최댓값 삭제
                    k = heapq.nlargest(1, min_heap)
                    min_heap.remove(int(k[0]))
                    heapq.heapify(min_heap)
                else:
                    # 최솟값 삭제
                    heapq.heappop(min_heap)
    return [max(min_heap), min(min_heap)] if min_heap else [0,0]