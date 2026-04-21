import sys
import heapq

input = sys.stdin.readline

p, m = map(int,input().split())

room = []

for _ in range(p):
    l,n = input().split()
    l = int(l)
    matching = 0
    if room != []:
        for r in room:
            if abs(r[0][0] - l) <= 10 and len(r) < m:
                r.append((l,n))
                matching = 1
                break
    if matching == 0:
        room.append([(l,n)])

for r in room:
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    q = []
    for player in r:
        heapq.heappush(q,(player[1],player[0]))
    while q != []:
        answer = heapq.heappop(q)
        print(answer[1],answer[0])