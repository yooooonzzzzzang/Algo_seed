def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    winner = {"6":1, "5":2, "4":3, "3":4,"2":5,"1":6,"0":6}
    # 6->1 5->2 4->3 3->4 2->
    zeroCnt = lottos.count(0)
    cnt = 0
    for i in lottos:
        if i in win_nums: 
            cnt+=1 
    print(zeroCnt)
    # if cnt >= 4 and zeroCnt:
        # answer.append(winner.get("6"))
    # else:
    answer.append(winner.get(str(cnt+zeroCnt)))
    answer.append(winner.get(str(cnt)))
    return answer