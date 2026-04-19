S = sorted(list(input()))

length = len(S)

def backtracking(cnt,visited,last_chr_A):
    if cnt == length:
        return 1
    ret_value = 0
    last_chr_B = 'A'
    for i in range(length):
        if visited[i] or S[i] == last_chr_B or S[i] == last_chr_A: continue
        last_chr_B = S[i]
        visited[i] = True
        ret_value += backtracking(cnt+1,visited,S[i])
        visited[i] = False
    return ret_value

last = 'A'

answer = 0

visited = [False] * length
for i in range(length):
    if last == S[i]: continue
    visited[i] = True
    last = S[i]
    answer += backtracking(1,visited,last)
    visited[i] = False

print(answer)