import sys

input = sys.stdin.readline

n = int(input())

answer = 0

for _ in range(n):
    a,b,c = map(int,input().split())
    num_list = [0] * 7
    num_list[a] += 1; num_list[b] += 1; num_list[c] += 1
    for i in range(1,7):
        if num_list[i] == 0: continue
        if num_list[i] == 1:
            answer = max(answer,100*i)
        elif num_list[i] == 2:
            answer = max(answer,1000+100*i)
        else:
            answer = max(answer,10000+1000*i)

print(answer)