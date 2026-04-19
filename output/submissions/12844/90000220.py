import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s = [0] * 2 ** math.ceil(math.log2(n)+1)
    init(array,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        t,*tmp = input().split()
        if t == '1':
            i,j,k = map(int,tmp)
            update(s,1,i,j,0,n-1,k)
        else:
            i,j = map(int,tmp)
            print(query(s,1,i,j,0,n-1))

def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    init(a,s,l_node,start,mid)
    init(a,s,r_node,mid+1,end)
    s[node] = s[l_node] ^ s[r_node]

def update(s,node,left,right,start,end,value):
    if left > end or right < start:
        return
    if (end-start) % 2 == 0: s[node] ^= value
    if left <= start and end <= right:
        return
    mid = (start+end) // 2
    l_node = node*2; r_node = node*2 + 1
    update(s,l_node,left,right,start,mid,value)
    update(s,r_node,left,right,mid+1,end,value)

def query(s,node,left,right,start,end):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return s[node]
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    return query(s,l_node,left,right,start,mid) ^ query(s,r_node,left,right,mid+1,end)

if __name__ == "__main__":
    main()