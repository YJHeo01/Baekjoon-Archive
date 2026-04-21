t = int(input())
for _ in range(t):
    n = int(input())
    lock = [True] * (n+1)
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            if lock[j] == True: lock[j] = False
            else: lock[j] = True
    answer = 0
    for i in range(1,n+1):
        if lock[i] == False: answer += 1
    print(answer)