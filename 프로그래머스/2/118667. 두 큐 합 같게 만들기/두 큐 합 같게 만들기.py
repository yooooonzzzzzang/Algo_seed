from collections import deque
def solution(queue1, queue2):
    answer = 0
    qa_sum = sum(queue1)
    qb_sum = sum(queue2)
    origin_qas = qa_sum
    origin_qbs = qb_sum
    target = (qa_sum + qb_sum)//2
    # a -> b
    # b -> a 

    def same_sum(q1, q2, target, qa_sum, qb_sum):
        cnt = 0
        qa =deque(q1)     
        qb =deque(q2)
        for i in range(len(queue1) * 3):
            if qa_sum == target:
                return cnt
            if qa_sum > qb_sum:
                tmp = qa.popleft()
                qb.append(tmp)
                qa_sum -= tmp
                qb_sum += tmp
                cnt +=1 
            else:
                tmp = qb.popleft()
                qa.append(tmp)
                qb_sum -= tmp
                qa_sum += tmp
                cnt +=1 
        return -1
    answer = same_sum(queue1,queue2,target,qa_sum,qb_sum )
    return answer