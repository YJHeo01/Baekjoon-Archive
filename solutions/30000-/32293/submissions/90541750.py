import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n = int(input())
    s = list(input().rstrip())
    answer = []
    while s:
        c = s.pop()
        if len(answer) >= 2 and c == 'A' and answer[-1] == 'B' and answer[-2] == 'B':
            answer.pop()
            answer.pop()
            s.append('B')
            s.append(c)    
        else:
            answer.append(c)
    while answer:
        print(answer.pop(),end="")
    print()