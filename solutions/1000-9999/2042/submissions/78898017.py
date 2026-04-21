import sys,math

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    a = get_a(n)
    h = math.ceil(math.log2(n))
    size = 2 ** (h+1)
    tree = [0] * size
    init(a,tree,1,0,n-1)
    for _ in range(m+k):
        command,b,c = map(int,input().split())
        if command == 1:
            a[b-1] = c
            update(a,tree,1,0,n-1,b-1)
        else:
            answer = query(tree,1,0,n-1,b-1,c-1)
            print(answer)

def get_a(n):
    a = []
    for _ in range(n):
        a.append(int(input()))
    return a

def init(a,tree,node,start,end):
    if start == end:
        tree[node] = a[start]
        return
    init(a,tree,node*2,start,(start+end)//2)
    init(a,tree,node*2+1,(start+end)//2+1,end)
    tree[node] = tree[node*2] + tree[node*2+1]

def update(a,tree,node,start,end,index):
    if index < start or index > end: return
    if start == end:
        tree[node] = a[index]
        return
    update(a,tree,node*2,start,(start+end)//2,index)
    update(a,tree,node*2+1,(start+end)//2+1,end,index)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree,node,start,end,left,right):
    if end < left or start > right: return 0
    if left <= start and end <= right: return tree[node]
    l_sum = query(tree,node*2,start,(start+end)//2,left,right)
    r_sum = query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return l_sum + r_sum

if __name__ == "__main__":
    main()