import sys,math

input = sys.stdin.readline

limit_value = 1000000007
def main():
    n,m,k = map(int,input().split())
    array = [int(input()) for _ in range(n)]
    size = 2 ** (math.ceil(math.log2(n))+1)
    segment_tree = [0] * size
    init(array,segment_tree,1,0,n-1)
    cnt = m + k
    for _ in range(cnt):
        a,b,c = map(int,input().split())
        if a == 1:
            array[b-1] = c
            update(array,segment_tree,1,b-1,0,n-1)
        else:
            answer = query(segment_tree,1,b-1,c-1,0,n-1)
            print(answer)

def init(array,segment_tree,node,start,end):
    if start == end:
        segment_tree[node] = array[start]
        return
    init(array,segment_tree,node*2,start,(start+end)//2)
    init(array,segment_tree,node*2+1,(start+end)//2+1,end)
    segment_tree[node] = (segment_tree[node*2] * segment_tree[node*2+1]) % limit_value

def update(array,segment_tree,node,target,start,end):
    if start > target or end < target: return
    if start == end:
        segment_tree[node] = array[start]
        return
    update(array,segment_tree,node*2,target,start,(start+end)//2)
    update(array,segment_tree,node*2+1,target,(start+end)//2+1,end)
    segment_tree[node] = (segment_tree[node*2] * segment_tree[node*2+1]) % limit_value

def query(segment_tree,node,left,right,start,end):
    if left > end or right < start: return 1
    if left <= start and end <= right: return segment_tree[node]
    return (query(segment_tree,node*2,left,right,start,(start+end)//2) * query(segment_tree,node*2+1,left,right,(start+end)//2+1,end)) % limit_value

if __name__ == "__main__":
    main()