import sys, heapq

input = sys.stdin.readline

alpha = dict()

q = int(input())

answer = 0

for _ in range(q):
    c, name, *tmp = input().split()
    if c == '1':
        if name not in alpha:
            alpha[name] = []
        for i in tmp[1:]:
            heapq.heappush(alpha[name],-int(i))
    else:
        if name not in alpha: continue
        for _ in range(int(tmp[0])):
            if alpha[name] == []: break
            answer -= heapq.heappop(alpha[name])
            
print(answer)
            