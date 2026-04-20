n = int(input())

answer = sum(list(map(int,input().split()))) / n

if answer - int(answer) <= 0.5:
    answer = int(answer)
else:
    answer = int(answer) + 1

print(answer)