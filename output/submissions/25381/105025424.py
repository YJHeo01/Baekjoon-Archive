# 백준 25381번 - ABBC
# 시간복잡도 - O(N)

S = list(input())

l = len(S)

answer = 0

use = [False] * l

def solution(use,L,R):
    ret_value = 0
    right = 0
    for left in range(l):
        if S[left] != L: continue
        right = max(right,left)
        while True:
            if right >= l: break
            if use[right] == False and S[right] == R: break
            right += 1
        if right >= l: break
        ret_value += 1
        use[left], use[right] = True, True
    return ret_value

answer = solution(use,'B','C') + solution(use,'A','B')

print(answer)