import sys,heapq

input = sys.stdin.readline

n = int(input())

day_work = [False] * 1001

heap = []

for _ in range(n):
    d,w = map(int,input().split())
    heapq.heappush(heap,(-w,d))
information = [0] * 1001
for i in range(1000,0,-1):
    information[i] = i #마감일이 같은 과제를 더 효율적으로 처리하기 위해 만든 리스트
answer = 0

while heap != []:
    w,d = heapq.heappop(heap)
    for i in range(information[d],0,-1):
        if day_work[i] == False:
            information[d] = i-1
            day_work[i] = True
            answer -= w
            break

print(answer)