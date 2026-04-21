import sys

input = sys.stdin.readline


n = int(input())

line_list = []

for _ in range(n):
    line_list.append(list(map(int,input().split())))

line_list.sort(key=lambda x:(x[0],-x[1]))

answer = 0
left, right = line_list[0][0], line_list[0][1]

for line in line_list:
    line_left, line_right = line
    if line_left <= right:
        right = max(right,line_right)
    else:
        answer += (right-left)
        left, right = line_left, line_right

answer += (right-left)

print(answer)