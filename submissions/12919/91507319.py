s = input()
t = input()


def backtracking(s,t):
    len_t = len(t)
    if len(s) == len_t:
        for i in range(len_t):
            if s[i] != t[i]: return 0
        return 1
    ret_value = 0
    if t[0] == 'B': 
        tmp = t[1:]
        tmp = tmp[::-1]
        ret_value = backtracking(s,tmp)
    if t[-1] == 'A':
        ret_value = max(ret_value,backtracking(s,t[:len_t-1]))
    return ret_value

answer = backtracking(s,t)

print(answer)