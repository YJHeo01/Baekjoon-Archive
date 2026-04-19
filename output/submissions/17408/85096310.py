import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = [[0,0] for _ in range(2 ** (math.ceil(math.log2(n))+1))]
    init(a,s,1,0,n-1)
    m = int(input())
    ans = []
    for _ in range(m):
        command,i,j = map(int,input().split())
        if command == 1:
            update(s,1,i-1,0,n-1,j)
        else:
            print(sum(query(s,1,i-1,j-1,0,n-1)))
    
def init(a,s,node,start,end):
    if start == end:
        s[node] = [a[end],0]
        return 
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init(a,s,l_node,start,mid)
    init(a,s,r_node,mid+1,end)
    tmp = sorted(s[l_node]+s[r_node])
    tmp.reverse()
    s[node] = tmp[:2]
    return

def update(s,node,target,start,end,value):
    if start > target or end < target:
        return
    if start == end:
        s[node] = [value,0]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update(s,l_node,target,start,mid,value)
    update(s,r_node,target,mid+1,end,value)
    tmp = sorted(s[l_node]+s[r_node])
    tmp.reverse()
    s[node] = tmp[:2]
    return

def query(s,node,left,right,start,end):
    if start > right or end < left:
        return [0]
    if left <= start and end <= right:
        return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    ret_value = sorted(query(s,l_node,left,right,start,mid)+query(s,r_node,left,right,mid+1,end))
    ret_value.reverse()
    return ret_value[:2]

if __name__ == "__main__":
    main()