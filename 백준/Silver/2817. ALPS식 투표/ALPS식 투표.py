votes = int(input())
n = int(input())
dic_totals = dict()
total =0
for _ in range(n):
    alp, vote = input().split()
    vote = int(vote)
    dic_totals[alp] = vote
    total += vote

cut = votes * 0.05
dic_totals = {k: v for k, v in dic_totals.items() if v >= cut}
alps = {}
for k,v in dic_totals.items():
    alps[k] = []
    for num in range(1,15):
        alps[k].append(v/num)

sorted_values_with_keys = []

for k, lst in alps.items():
    for val in lst:
        sorted_values_with_keys.append((val, k))  # (값, 키) 쌍 저장

sorted_values_with_keys.sort(reverse=True)  # 내림차순 정렬 (원하면 오름차순도 가능)

cnt = {k:0 for k in  dic_totals.keys()}
for i in range(14):
    v = sorted_values_with_keys[i][0]
    k = sorted_values_with_keys[i][1]
    cnt[k] += 1
# 딕셔너리 cnt를 값 기준으로 내림차순 정렬
sorted_cnt = sorted(cnt.items(), key=lambda x:  x[0])  # tie-breaker: 알파벳순

for key, val in sorted_cnt:
    print(f"{key} {val}")

