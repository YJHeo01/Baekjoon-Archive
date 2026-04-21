import math, sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    s_length = 2 ** (math.ceil(math.log2(n+1))+1)
    s = [0] * s_length
    a = [0] * (n+1)
    for _ in range(m):
        c,i,j = map(int,input().split())
        if c == 0:
            if i > j: i,j = j,i
            print(func_sum(s,1,i,j,1,n))
        else:
            func_modify(a,s,1,i,1,n,j)

def func_sum(s,node,left,right,start,end):
    if left > end or start > right: return 0
    if left <= start and end <= right: s[node]
    if start == end: return s[node]
    mid = (start+end) // 2; l_node = node * 2; r_node = node * 2 + 1
    return func_sum(s,l_node,left,right,start,mid) + func_sum(s,r_node,left,right,mid+1,end)

def func_modify(a,s,node,target,start,end,value):
    if start > target or end < target: return
    if start == end:
        a[target] = value
        s[node] = value
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    func_modify(a,s,l_node,target,start,mid,value)
    func_modify(a,s,r_node,target,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]

if __name__ == "__main__":
    main()