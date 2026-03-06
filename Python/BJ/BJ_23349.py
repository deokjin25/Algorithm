import sys
input = sys.stdin.readline
n = int(input())

students = {}
vote = {}
table = {}

for i in range(n) :
  name, place, s, e = input().split()

  # 중복 투표의 경우
  if students.get(name, 0) != 0 : continue
  students[name] = 1

  s, e = int(s), int(e)

  if vote.get(place, 0) == 0 :  #처음 투표된 장소
    vote[place] = [(s,e)]
    table[place] = [0] * 10
    for i in range(s,e) :
      table[place][i] = 1
  
  else : #이전에 투표 된 적 있는 경우
    vote[place].append((s,e))
    for i in range(s,e) :
      table[place][i] += 1

# print(vote)
# print(table)

sorted_table = sorted(table.items(), key = lambda x : (-max(x[1]), x[0]))
answer_lst = sorted_table[0]
answer_place = answer_lst[0]
x = max(answer_lst[1])

vote_times = vote[answer_place]
vote_times.sort()

vote_time_table = [0] * 50001
for vote_time in vote_times :
  vts, vte = vote_time
  for i in range(vts, vte) :
    vote_time_table[i] += 1
  if x == max(vote_time_table) :
    break

s = vote_time_table.index(x)
e = s + vote_time_table.count(x)

print(answer_lst[0], s, e)