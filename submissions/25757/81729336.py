import sys

input = sys.stdin.readline

n, game = input().rstrip().split()

change = {'Y':1,'F':2,'O':3}

people = dict()

answer = 0

for _ in range(int(n)):
    tmp = input().rstrip()
    if tmp not in people:
        people[tmp] = True
        answer += 1

print(answer//change[game])