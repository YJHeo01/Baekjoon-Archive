import sys

sys.setrecursionlimit(10**6)

s = input()
target = input()
length = len(s)
target_length = len(target)
def backtracking(s,target,cnt,idx):
    if idx + target_length >= length:
        return cnt
    ret_value = max(cnt,backtracking(s,target,cnt,idx+1))
    if s[idx:idx+target_length] == target:
        ret_value = max(ret_value,backtracking(s,target,cnt+1,idx+target_length))
    return ret_value

print(backtracking(s,target,0,0))