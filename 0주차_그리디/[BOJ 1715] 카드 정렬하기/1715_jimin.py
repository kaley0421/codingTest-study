import heapq

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

heapq.heapify(cards)
answer = 0

while len(cards) >= 2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    heapq.heappush(cards,a+b)
    answer += (a+b)
    
print(answer)