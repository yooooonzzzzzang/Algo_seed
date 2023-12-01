def solution(bandage, health, attacks):
    answer = 0
    full_health = health
    tech_time, per_recover, bonus = bandage[0], bandage[1], bandage[2]
    time = 0
    flag= 1
    combo = 0
    for attack_time, damage in attacks:
        
        while 1:
            # 죽음 조건 
            if health <= 0:
                return -1
            time += 1
            
            # 공격 받는다 
            if time == attack_time:
                combo = 0
                health -= damage
                break
                
            health = min(full_health, health+per_recover)
            combo += 1
            
            # 콤보 5 연속
            if combo == tech_time:
                combo = 0
                health = min(full_health, health+ bonus)   
    if health <= 0:
        return -1
    return health