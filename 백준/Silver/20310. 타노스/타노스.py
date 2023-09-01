from itertools import permutations
s = input()
one_cnt = s.count("1")
zero_cnt = len(s) - one_cnt
arr = []
while one_cnt > 1 or zero_cnt > 1:
    one_cnt = one_cnt//2
    zero_cnt = zero_cnt//2
    arr.append(zero_cnt*"0"+one_cnt*"1")
arr.sort()
for i in arr:
    if "0" in i and "1" in i:
        print(i)
        break