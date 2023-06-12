def solution(common):
    is_Be  =False
    is_cha = False
    k = []
    for i in range(1,len(common)):
        print(common[i] - common[i-1])
        
        if k and k[-1] == (common[i] - common[i-1]):
        # if not k:
            is_cha = True
            is_Be = False
        else: 
            is_cha = False
            is_Be = True
        k.append(common[i] - common[i-1])
        
    if is_cha:
        return common[-1] + k[-1]
    elif is_Be:
        be = common[1]//common[0]
        return be * common[-1]
