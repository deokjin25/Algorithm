import sys
input = sys.stdin.readline

# s = input().rstrip() + '-'
# cur = ''
# answer = 0
# minus_flag = False

# for i in range(len(s)) :
#   x = s[i]

#   if x.isdigit() :
#     cur += x
#     continue

#   if minus_flag :
#     answer -= int(cur)
#     cur = ''
#   else :
#     answer += int(cur)
#     cur = ''

#   if x == '-' :
#     minus_flag = True

# print(answer)

s = input().rstrip()
parts = s.split('-')          # '-' 기준으로 분리
answer = sum(map(int, parts[0].split('+')))  # 첫 번째 그룹은 더하기
for part in parts[1:]:
    answer -= sum(map(int, part.split('+')))  # 이후 그룹은 전부 빼기
print(answer)