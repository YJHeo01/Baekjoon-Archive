import sys

input = sys.stdin.readline

n = int(input())

line_list = []

for _ in range(n):
    x,y = map(int,input().split())
    line_list.append((x,y))
    
sorted(line_list)

start_idx = 0

answer = 0

for i in range(1,n):
    if line_list[i][0] > line_list[i-1][1]:
        answer += ( line_list[i-1][1] - line_list[start_idx][0])
        start_idx = i
        
answer += (line_list[n-1][1] - line_list[start_idx][0])
        
print(answer)