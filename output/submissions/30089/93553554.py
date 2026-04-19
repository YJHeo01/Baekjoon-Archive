import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = list(input().rstrip())
    length = len(s)
    for i in range(length+1):
        tmp = s[:i]
        tmp.reverse()
        answer = s + tmp
        left, right = 0,length+i-1
        finish = True
        while left <= right:
            if answer[left] != answer[right]:
                finish = False
                break
            left += 1
            right -= 1
        if finish:
            for c in answer:
                print(c,end="")
            print()
            break