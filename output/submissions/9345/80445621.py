import sys,math

input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        solution()

def solution():
    n,k = map(int,input().split())
    array = init_array(n)
    s_size = 2 ** (1+math.ceil(math.log2(n)))
    max_s, min_s = [0] * s_size, [0] * s_size
    init_min_s(array,min_s,1,0,n-1)
    init_max_s(array,max_s,1,0,n-1)

    for _ in range(k):
        q,a,b = map(int,input().split())
        if q == 0:
            array[a],array[b] = array[b],array[a]
            update_max_s(array,max_s,1,a,b,0,n-1)
            update_min_s(array,min_s,1,a,b,0,n-1)
        else:
            if b != query_max_s(max_s,1,a,b,0,n-1) or a != query_min_s(min_s,1,a,b,0,n-1):
                print("NO")
            else:
                print("YES")

def init_array(n):
    array = [0] * n
    for i in range(n): array[i] = i
    return array

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

def update_max_s(a,s,node,left,right,start,end):
    if left > end or right < start: return
    if start == end:
        s[node] = a[end]
        return
    update_max_s(a,s,node*2,left,right,start,(start+end)//2)
    update_max_s(a,s,node*2+1,left,right,(start+end)//2+1,end)
    s[node] = max(s[node*2],s[node*2+1])

def update_min_s(a,s,node,left,right,start,end):
    if left > end or right < start: return
    if start == end:
        s[node] = a[end]
        return
    update_min_s(a,s,node*2,left,right,start,(start+end)//2)
    update_min_s(a,s,node*2+1,left,right,(start+end)//2+1,end)
    s[node] = min(s[node*2],s[node*2+1])

def query_max_s(s,node,left,right,start,end):
    if left > end or right < start:
        return 0
    if (left <= start and end <= right) or s[node] < right:
        return s[node]
    return max(query_max_s(s,node*2,left,right,start,(start+end)//2),query_max_s(s,node*2+1,left,right,(start+end)//2+1,end))


def query_min_s(s,node,left,right,start,end):
    if left > end or right < start: return 200000
    if (left<=start and end <= right) or s[node] > left:
        return s[node]
    return min(query_min_s(s,node*2,left,right,start,(start+end)//2),query_min_s(s,node*2+1,left,right,(start+end)//2+1,end))

if __name__ == "__main__":
    main()