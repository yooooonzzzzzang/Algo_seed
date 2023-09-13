from collections import Counter
from itertools import combinations
def solution(orders, course):
    result = []

    for i in course:
        combis = []
        for order in orders:
            combis += combinations(sorted(order), i)
        most_common_order = Counter(combis).most_common()
        result += [ k for k, v in most_common_order if v >= 2 and v == most_common_order[0][1] ]
    return [ ''.join(v) for v in sorted(result) ]

