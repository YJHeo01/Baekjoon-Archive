n = int(input())

student = list(map(int,input().split()))

stack = []

food = []

for i in range(n-1):
    if student[i] > student[i+1]:
        stack.append(student[i])
    else:
        food.append(student[i])
    
food.append(student[n-1])

while stack != []:
    food.append(stack.pop())

answer = "Nice"
for i in range(n-1):
    if food[i] > food[i+1]:
        answer = "Sad"
        break

print(answer)