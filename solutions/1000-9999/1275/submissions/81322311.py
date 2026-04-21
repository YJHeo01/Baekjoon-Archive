import sys, math

input = sys.stdin.readline

def main():
    n,q = map(int,input().split())
    array = list(map(int,input().split()))
    s_length = 2 ** math.ceil(math.log2(n)+1)
    s = [0] * s_length
    init(array,s,1,0,n-1)
    for _ in range(q):
        x,y,a,b = map(int,input().split())
        if x > y: x,y = y,x
        print(query(s,1,x-1,y-1,0,n-1))
        change(array,s,1,a-1,0,n-1,b)

def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    init(a,s,node*2,start,(start+end)//2)
    init(a,s,node*2+1,(start+end)//2+1,end)
    s[node] = s[node*2] + s[node*2+1]
    
def query(s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    return query(s,node*2,left,right,start,(start+end)//2) + query(s,node*2+1,left,right,(start+end)//2+1,end)

def change(a,s,node,target,start,end,value):
    if start > target or end < target: return
    if start == end:
        a[target] = value
        s[node] = value
        return
    change(a,s,node*2,target,start,(start+end)//2,value)
    change(a,s,node*2+1,target,(start+end)//2+1,end,value)
    s[node] = s[node*2] + s[node*2+1]
    
if __name__ == "__main__":
    main()