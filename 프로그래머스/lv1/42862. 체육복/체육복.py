# def solution(n, lost, reserve):
#     answer = 0
#     # 1. 여벌 체육복 - 도난
#     for i in lost:
#         if i in reserve:
#             del reserve[reserve.index(i)]
#             del lost[lost.index(i)]
    
#     # 2. 최댓값 디용 앞에 있는 애를 빌려줘야할듯
#     for i in range(len(lost)):
        
#     return answer

def solution(n, lost, reserve): 
    answer = 0 
    
    reserve_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    
    for i in reserve_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
            
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
            
    answer = n - len(lost_del)
    
    return answer