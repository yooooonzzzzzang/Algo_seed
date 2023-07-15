from collections import Counter
def solution(X, Y):
    answer = ''
    q = []
    x_count = Counter(X)
    y_count = Counter(Y)
    k = list((x_count&y_count).elements())
    k = list(map(int, k))
    k.sort(reverse=True)
    if not k :
        return "-1"
    if k[0] == 0:
        print(k)
        return "0"
    return ''.join(str(i) for i in k)
    