import sys

input = sys.stdin.readline

n = int(input())

line_list = []

for _ in range(n):
    line_list.append(int(input()))

line_list.sort(reverse=True)

answer = -1

for i in range(n-2):
    if line_list[i] < line_list[i+1] + line_list[i+2]:
        answer = sum(line_list[i:i+3])
        break

print(answer)