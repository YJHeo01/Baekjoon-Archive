import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    max_s = [0] * s_length
    min_s = [0] * s_length
    init_min_s(array,min_s,1,0,n-1)
    init_max_s(array,max_s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        i,j,k = map(int,input().split())
        print(query(max_s,min_s,1,i-1,j-1,0,n-1,k))
    
def init_min_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    init_min_s(a,s,node*2,start,(start+end)//2)
    init_min_s(a,s,node*2+1,(start+end)//2+1,end)
    s[node] = min(s[node*2],s[node*2+1])

def init_max_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    init_max_s(a,s,node*2,start,(start+end)//2)
    init_max_s(a,s,node*2+1,(start+end)//2+1,end)
    s[node] = max(s[node*2],s[node*2+1])

def query(max_s,min_s,node,left,right,start,end,target):
    if start > right or end < left or max_s[node] <= target: return 0
    if left <= start and end <= right and min_s[node] > target:
        return (end-start+1)
    return query(max_s,min_s,node*2,left,right,start,(start+end)//2,target) + query(max_s,min_s,node*2+1,left,right,(start+end)//2+1,end,target)

if __name__ == "__main__":
    main()