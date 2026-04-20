n = int(input())

tower = list(map(float,input().split()))

answer = 0
for i in range(n):
    finish = 0
    num = 0
    for j in range(i-1,-1,-1):
        for k in range(i-1,j,-1):
            tmp = tower[i] + (tower[j]-tower[i]) * (k-i) / (j-i)
            if tower[k] >= tmp:
                finish = 1
                break
        if finish == 1:
            finish = 0
        else:
            num+=1
    finish = 0
    for j in range(i+1,n):
        for k in range(i+1,j):
            tmp = tower[i] + (tower[j]-tower[i]) *(k-i)/ (j-i)
            if tower[k] >= tmp:
                finish = 1
                break
        if finish == 1:
            finish = 0
        else:
            num+=1
    answer = max(answer,num)

print(answer)