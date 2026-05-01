def solution(answers):
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0,0,0]
    for i in range(len(answers)) :
        answer = answers[i]
        
        if answer == person_1[i%len(person_1)] :
            score[0]+=1
        if answer == person_2[i%len(person_2)] :
            score[1]+=1
        if answer == person_3[i%len(person_3)] :
            score[2]+=1
    
    answer = []
    for idx, val in enumerate(score) :
        if val == max(score) :
            answer.append(idx+1)
    
    return answer