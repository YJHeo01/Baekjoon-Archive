s = input()
t = input()

table = set()

def backtracking(table,s,t):
    len_t = len(t)
    if len(s) == len_t:
        for i in range(len_t):
            if s[i] != t[i]: return 0
        return 1
    ret_value = 0
    if t[0] == 'B': 
        tmp = t[1:]
        tmp = tmp[::-1]
        if tmp not in table: 
            table.add(tmp)
            ret_value = backtracking(table,s,tmp)
    if t[-1] == 'A' and t[:len_t-1] not in table:
        table.add(t[:len_t-1]) 
        ret_value = max(ret_value,backtracking(table,s,t[:len_t-1]))
    return ret_value

answer = backtracking(table,s,t)

print(answer)