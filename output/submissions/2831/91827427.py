n = int(input())

men = sorted(list(map(int,input().split())))

women = sorted(list(map(int,input().split())))

j = 0

while True:
    if  j == n or women[j] > 0:
        break
    j += 1

answer = 0

for i in range(n-1,-1,-1):
    if men[i] > 0: continue
    if j == n: break
    if abs(men[i]) > women[j]:
        answer += 1
        j += 1
        
j = 0

while True:
    if j == n or men[j] > 0: break
    j += 1

for i in range(n-1,-1,-1):
    if women[i] > 0: continue
    if j == n: break
    if abs(men[i]) > women[j]:
        answer += 1
        j += 1

print(answer)