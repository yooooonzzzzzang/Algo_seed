import heapq
import sys
heap = []
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            # 최대값 출력하고 제거
            print(heapq.heappop(heap)[1])

        else:
            print(0)
            heapq.heappush(heap,(0,0))
    else:
        heapq.heappush(heap,(-n,n))