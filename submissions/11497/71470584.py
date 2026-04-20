#https://github.com/YJHeo01


t = int(input())

for _ in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    trees = []
    L.sort()
    for i in range(0,n,2):
        trees.append(L[i])
    n -= 1
    plus = 0
    if n % 2 == 0:
        n -= 1
        plus += 1
    for i in range(n,0,-2):
        trees.append(L[i])
    n += plus
    answer = 0
    for i in range(-1,n):
        answer = max(answer,abs(trees[i+1]-trees[i]))
    print(answer)