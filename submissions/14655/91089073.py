input()
answer = 0
for _ in range(2):
    for i in map(int,input().split()) :answer += abs(i)
print(answer)