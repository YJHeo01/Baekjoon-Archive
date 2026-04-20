n, k = map(int,input().split())

food_human = list(input())

people = []

answer = 0
for i in range(n):
    if food_human[i] == 'P':
        people.append(i)

for i in people:
    for j in range(i-k,i+k+1):
        if j < 0 or j >= n:
            continue
        if food_human[j] == 'H':
            food_human[j] = 'X'
            answer+=1
            break
print(answer)