n = int(input())

cookie = []

for i in range(n):
    tmp = list(input())
    cookie.append(tmp)
heart = (0,0)
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            heart = (i+1,j)
            break
    if heart != (0,0):
        break
left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0
h = 0
h_ = 0
for i in range(heart[1]-1,-1,-1):
    if cookie[heart[0]][i] == '_':
        break
    left_arm += 1

for i in range(heart[1]+1,n):
    if cookie[heart[0]][i] == '_':
        break
    right_arm += 1

for i in range(heart[0]+1,n):
    if cookie[i][heart[1]] == '_':
        h_ = i
        break
    h += 1

for i in range(h_,n):
    if cookie[i][heart[1]-1] == '_':
        break
    left_leg += 1

for i in range(h_,n):
    if cookie[i][heart[1]+1] == '_':
        break
    right_leg += 1

print(heart[0]+1,heart[1]+1)
print(left_arm,right_arm,h,left_leg,right_leg)