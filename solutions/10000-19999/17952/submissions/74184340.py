import sys

input = sys.stdin.readline

n = int(input())

score = 0

stack = []
quest = [0,0,0]
for _ in range(n):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        stack.append(quest)
        quest = tmp
    quest[2] -= 1
    if quest[2] == 0:
        score += quest[1]
        if stack != []:
            quest = stack.pop()

print(score)