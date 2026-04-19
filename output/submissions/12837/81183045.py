import sys, math

input = sys.stdin.readline

def main():
    n,q = map(int,input().split())
    s_length = 2 ** (1+math.ceil(math.log2(n)))
    a = [0] * n
    s = [0] * s_length
    for _ in range(q):
        command, p, x = map(int,input().split())
        if command == 1:
            a[p-1] += x
            update(a,s,1,p-1,0,n-1)
        else:
            print(query(s,1,p-1,x-1,0,n-1))

def update(a,s,node,target,start,end):
    if start > target or end < target: return
    if start == end:
        s[node] = a[target]
        return
    update(a,s,node*2,target,start,(start+end)//2)
    update(a,s,node*2+1,target,(start+end)//2+1,end) 
    s[node] = s[node*2] + s[node*2+1]

def query(s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    return query(s,node*2,left,right,start,(start+end)//2) + query(s,node*2+1,left,right,(start+end)//2+1,end)

if __name__ == "__main__":
    main()