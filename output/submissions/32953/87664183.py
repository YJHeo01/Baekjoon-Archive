n,m = map(int,input().split())

study = dict([])

for _ in range(n):
    input()
    tmp = list(input().split())
    for s in tmp:
        if s in study:
            study[s] +=1
        else:
            study[s] = 1

answer = 0

for s in study:
    if study[s] >= m: answer += 1
    
print(answer)