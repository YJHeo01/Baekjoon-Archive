S = list(input())

l = len(S)

answer = 0

use = [False] * l

left, right = 0, 0

for left in range(l):
    if S[left] != 'B': continue
    right = max(right,left)
    while True:
        if right >= l: break
        if use[right] == False and S[right] == 'C': break
        right += 1
    if right >= l: break
    answer += 1
    use[left], use[right] = True, True
    
left, right = 0,0

for left in range(l):
    if S[left] != 'A': continue
    right = max(right,left)
    while True:
        if right >= l: break
        if use[right] == False and S[right] == 'B': break
        right += 1
    if right >= l: break
    answer += 1
    use[left], use[right] = True, True

print(answer)