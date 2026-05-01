from itertools import permutations

def solution(babbling):
    answer = 0
    c = ['aya','ye','woo','ma']
    x = []
    for i in range(1,5) :
      for p in permutations(c, i) :
         x.append(''.join(p))

    for babb in babbling :
      if babb in x :
         answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))