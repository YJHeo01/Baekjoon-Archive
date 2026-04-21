import sys

input = sys.stdin.readline

n = int(input())

line_list = []

for _ in range(n):
    x,y = map(int,input().split())
    line_list.append((x,y))
    
sorted(line_list)

start = line_list[0][0]
last = line_list[0][1]
answer = 0

for i in range(1,n):
    if line_list[i][0] > last:
        answer += (last - start)
        start = line_list[i][0]
        last = line_list[i][1]
    else:
        last = max(last,line_list[i][1])
        start = min(line_list[i][0],start)
        
answer += (last - start)
        
print(answer)
        