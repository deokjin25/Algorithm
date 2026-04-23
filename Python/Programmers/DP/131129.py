def solution(target):
    scores = set()
    for x in list(range(1,21)) :
        scores.add(x)
        scores.add(x*2)
        scores.add(x*3)
    scores.add(50)
    scores = list(scores)
    
    shoot_cnt = [0] * 100001
    single_bull = [0] * 100001
    
    #20: 싱글
    for score in range(1,21) :
        shoot_cnt[score] = 1
        single_bull[score] = 1
    
    #21~40: 더블/트리플 or 2싱글
    for score in range(21, 41) :
        if score in scores :
            shoot_cnt[score] = 1
        else :
            shoot_cnt[score] = 2
            single_bull[score] = 2
    
    #41~49: 더블/트리플 or 더블/트리플 + 1싱글
    for score in range(41, 50) :
        if score in scores :
            shoot_cnt[score] = 1
        else :
            shoot_cnt[score] = 2
            single_bull[score] = 1
    #50: 불
    shoot_cnt[50] = 1
    single_bull[50] = 1
    
    #51~60: 더블/트리플 or 불+싱글
    for score in range(51, 61) :
        if score in scores :
            shoot_cnt[score] = 1
        else :
            shoot_cnt[score] = 2
            single_bull[score] = 2
    
    #이후 dp
    for score in range(61, 100001) :
        cnt_50 = shoot_cnt[score-50]
        cnt_60 = shoot_cnt[score-60]
        
        if cnt_50 <= cnt_60 :
            shoot_cnt[score] = cnt_50+1
            single_bull[score] = single_bull[score-50] + 1
        else :
            shoot_cnt[score] = cnt_60+1
            single_bull[score] = single_bull[score-60]

    return [shoot_cnt[target], single_bull[target]]