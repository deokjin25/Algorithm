#36
import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

jewel = []
for _ in range(n) :
  m, v = map(int, input().split())
  jewel.append((m,v))

jewel.sort(reverse=True)

bag = []
for _ in range(k) :
  c = -int(input())
  bag.append(c)

heapq.heapify(bag)

answer = []
for w, cost in jewel :
  if bag and w <= -bag[0] :
    heapq.heappop(bag)
    heapq.heappush(answer, cost)
    continue

  if answer and answer[0] < cost :
    heapq.heappop(answer)
    heapq.heappush(answer, cost)

print(sum(answer))


# import sys
# input = sys.stdin.readline
# import heapq

# n, k = map(int, input().split())

# jewel = []
# for _ in range(n):
#     m, v = map(int, input().split())
#     jewel.append((m, v))

# # 보석을 무게 오름차순으로 정렬
# jewel.sort()

# bag = []
# for _ in range(k):
#     c = int(input())
#     bag.append(c)

# # 가방을 용량 오름차순으로 정렬
# bag.sort()

# answer = 0
# max_heap = []  # 최대 힙 (가격)
# jewel_idx = 0

# # 작은 가방부터 처리
# for capacity in bag:
#     # 현재 가방에 넣을 수 있는 모든 보석을 힙에 추가
#     while jewel_idx < n and jewel[jewel_idx][0] <= capacity:
#         # 최대 힙을 위해 음수로 저장
#         heapq.heappush(max_heap, -jewel[jewel_idx][1])
#         jewel_idx += 1
    
#     # 넣을 수 있는 보석 중 가장 비싼 것 선택
#     if max_heap:
#         answer += -heapq.heappop(max_heap)

# print(answer)