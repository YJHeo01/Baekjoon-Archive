s = list(input())

length = len(s)

a_cnt = 0
b_cnt = 0
c_cnt = 0

for c in s:
    if c == 'A': a_cnt += 1
    elif c == 'B': b_cnt += 1
    else: c_cnt += 1

def dfs(array,idx,a_cnt,b_cnt,c_cnt,last_b,last_c):
    if idx == length:
        for c in array:
            print(c,end="")
        exit(0)
    if c_cnt > 0 and last_c + 2 < idx:
        dfs(array+['C'],idx+1,a_cnt,b_cnt,c_cnt-1,last_b,idx)
    if b_cnt > 0 and last_b + 1 != idx:
        dfs(array+['B'],idx+1,a_cnt,b_cnt-1,c_cnt,idx,last_c)
    if a_cnt > 0: dfs(array+['A'],idx+1,a_cnt-1,b_cnt,c_cnt,last_b,last_c)

dfs([],0,a_cnt,b_cnt,c_cnt,-3,-100)

print(-1)