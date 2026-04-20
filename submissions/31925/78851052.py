import sys, heapq

input = sys.stdin.readline

n = int(input())

player = []

m = 0
for _ in range(n):
    name, jh, ic, sh, ap = input().split()
    if jh == 'hewhak': continue
    if ic == 'winner': continue
    sh = int(sh)
    if sh <= 3 and sh > 0: continue
    ap = int(ap)
    heapq.heappush(player,(ap,name))
    m += 1
    
if m > 10: m = 10

print(m)

answer = []
for _ in range(m):
    ap, name = heapq.heappop(player)
    answer.append(name)
    
answer.sort()

for i in answer:
    print(i)