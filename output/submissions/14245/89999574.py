import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s = [0] * 2 ** math.ceil(math.log2(n)+1)
    m = int(input())
    for _ in range(m):
        t,*tmp = input().split()
        if t == '1':
            a,b,c = map(int,tmp)
            update(s,1,a,b,0,n-1,c)
        else:
            a = int(tmp[0])
            print(query(s,1,0,n-1,a)^array[a])

def update(s,node,left,right,start,end,value):
    if left > end or right < start:
        return
    if left <= start and end <= right:
        s[node] ^= value
        return
    mid = (start+end) // 2
    l_node = node*2; r_node = node*2 + 1
    update(s,l_node,left,right,start,mid,value)
    update(s,r_node,left,right,mid+1,end,value)

def query(s,node,start,end,target):
    if start == end:
        return s[node]
    mid = (start+end) // 2
    if target <= mid: return s[node] ^ query(s,node*2,start,mid,target)
    else: return s[node] ^ query(s,node*2+1,mid+1,end,target)

if __name__ == "__main__":
    main()