import sys

input = sys.stdin.readline

n = int(input())

user = set([])

answer = 0

for _ in range(n):
    tmp = input().rstrip()
    if tmp == 'ENTER':
        user = set([])
        continue
    if tmp not in user:
        user.add(tmp)
        answer += 1

print(answer)