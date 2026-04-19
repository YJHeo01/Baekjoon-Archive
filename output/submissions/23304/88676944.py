s = list(input())

length = len(s)

def backtracking(s,start,end):
    if start==end: return True
    left,right = start,end
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    left -= 1; right += 1
    return backtracking(s,start,left) and backtracking(s,right,end)

AKARAKA = backtracking(s,0,length-1)

if AKARAKA:
    print("AKARAKA")
else:
    print("IPSELENTI")