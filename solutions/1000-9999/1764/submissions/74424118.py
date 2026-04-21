import sys

input = sys.stdin.readline

n,m = map(int,input().split())

first_line_answer = 0
second_line_answer = []

human_list = {}

for _ in range(n):
    name = input().rstrip()
    human_list[name] = True

for _ in range(m):
    name = input().rstrip()
    if name in human_list:
        first_line_answer += 1
        second_line_answer.append(name)

second_line_answer.sort()

print(first_line_answer)

for name in second_line_answer:
    print(name)