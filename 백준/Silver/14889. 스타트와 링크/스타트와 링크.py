from itertools import permutations
from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 순열로 
def solution(tmp):
    score = 0
    for v1, v2 in list(permutations(tmp, 2)):
        score += arr[v1][v2]
    return score 

teams_n = n//2
combis = list(combinations(range(n), teams_n))
differ = 10000000000
for i in range(len(combis)//2):
    start_team = combis[i]
    link_team = combis[len(combis)-i-1]

    differ = min(differ, abs(solution(start_team) - solution(link_team)))

print(differ)