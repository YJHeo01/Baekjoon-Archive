n = int(input())
room = [0] * (10**9 + 1)
answer = 0
for i in range(n):
    s,t = map(int,input().split())
    room[s] += 1
    room[t] += 1
    answer = max(answer,room[s],room[t])
    
print(answer)