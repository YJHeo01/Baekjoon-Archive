import sys, math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    s = [0] * s_length
    init_s(array,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        i,j,k = map(int,input().split())
        print(query(s,1,i-1,j-1,0,n-1,k))
    
def init_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    init_s(a,s,node*2,start,(start+end)//2)
    init_s(a,s,node*2+1,(start+end)//2+1,end)
    s[node] = min(s[node*2],s[node*2+1])

def query(s,node,left,right,start,end,target):
    if left <= start and end <= right and s[node] > target:
        return (end-start+1)
    if start > right or end < left or start == end: return 0
    return query(s,node*2,left,right,start,(start+end)//2,target) + query(s,node*2+1,left,right,(start+end)//2+1,end,target)

if __name__ == "__main__":
    main()