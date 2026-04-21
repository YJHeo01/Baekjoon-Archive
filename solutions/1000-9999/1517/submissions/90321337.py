import math, sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))



s_size = 2 ** math.ceil(math.log2(n)+1)

max_s = [0] * s_size
min_s = [0] * s_size

def init(a,max_s,min_s,node,start,end):
    if start == end:
        max_s[node] = a[end]
        min_s[node] = a[end]
        return
    l_node, r_node = node * 2, node * 2 + 1
    mid = (start+end) // 2
    init(a,max_s,min_s,l_node,start,mid)
    init(a,max_s,min_s,r_node,mid+1,end)
    max_s[node] = max(max_s[l_node],max_s[r_node])
    min_s[node] = min(min_s[l_node],min_s[r_node]) 
    
init(a,max_s,min_s,1,0,n-1)

a.sort()

def solution(max_s,min_s,node,start,end):
    if start == end:
        if max_s[node] == start + 1: return 0
        else: return 1
    if max_s[node] != a[end] or min_s[node] != a[start]: return end - start + 1
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    return solution(max_s,min_s,l_node,start,mid) + solution(max_s,min_s,r_node,mid+1,end)

print(solution(max_s,min_s,1,0,n-1))