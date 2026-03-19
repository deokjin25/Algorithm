# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# true_list = set(list(map(int, input().split()))[1:])

# def is_ok_lie(party_people) :
#   for party in party_people :
#     if party in true_list :
#       return False
#   return True

# def party_lie(party) :
#   for people in party :
#     if people not in lie_people or lie_people[people] == 0 :
#       return False
#   return True

# lie_people = {}
# all_party = []
# #거짓말할 수 있는 사람들 판별
# #lie_people[n] == 1 이면 거짓말 가능
# for _ in range(m) :
#   party_people = list(map(int, input().split()))[1:]
#   all_party.append(party_people)
#   if is_ok_lie(party_people) :
#     for people in party_people :
#       if people not in lie_people :
#         lie_people[people] = 1
#   else :
#     for people in party_people :
#       true_list.add(people) #진실 set에 추가
#       if people in lie_people :
#         lie_people[people] = 0

# #거꾸로
# for party_people in all_party[::-1] :
#   if is_ok_lie(party_people) :
#       for people in party_people :
#         if people not in lie_people :
#           lie_people[people] = 1
#   else :
#     for people in party_people :
#       true_list.add(people) #진실 set에 추가
#       if people in lie_people :
#         lie_people[people] = 0

# #거짓말 할 수 있는 사람들만 모인 파티들 선별
# answer = 0
# for party in all_party :
#   if party_lie(party) :
#     answer+=1
# print(answer)

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

n, m = map(int, input().split())

true_info = list(map(int, input().split()))
true_count = true_info[0]
truth_set = set(true_info[1:])

parent = list(range(n + 1))

parties = []
for _ in range(m):
    people = list(map(int, input().split()))[1:]
    parties.append(people)
    # 같은 파티 사람들을 모두 union
    for i in range(1, len(people)):
        union(people[0], people[i])

answer = 0
for party in parties:
    # 파티원 중 한 명이라도 진실 아는 사람의 컴포넌트면 거짓말 불가
    if all(find(p) not in {find(t) for t in truth_set} for p in party):
        answer += 1

print(answer)