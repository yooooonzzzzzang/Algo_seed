from collections import Counter
def solution(X, Y):
    x_count = Counter(X)
    y_count = Counter(Y)
    k = list((x_count&y_count).elements())
    k.sort(reverse=True)
    if not k :
        return "-1"
    if k[0] == "0":
        return "0"
    return ''.join(k)
    