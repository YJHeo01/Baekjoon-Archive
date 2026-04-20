import sys

input = sys.stdin.readline

S = input().rstrip()

target = [0] * 26

for c in S:
    target[ord(c)-ord('a')] += 1

n = int(input())

for _ in range(n):
    tmp = input().rstrip()
    password = [0] * 26
    for c in tmp:
        password[ord(c)-ord('a')] += 1
    change = False
    tmp = 0
    for _ in range(3):
        for i in range(26):
            if target[i] > password[i]:
                if tmp > 0 and (change == False):
                    password[i] += 1
                    tmp -= 1
                    change = True
            elif password[i] > target[i]:
                tmp += (password[i] - target[i])
                password[i] = target[i]
    answer = "YES"
    if len(S) > len(password): answer = "NO"
    if change == False and tmp == 0: answer = "NO"
    for i in range(26):
        if target[i] > password[i]:
            answer = "NO"
    
    print(answer)