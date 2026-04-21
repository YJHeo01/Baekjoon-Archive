import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    data = [0] * INF
    length = 2 ** (math.ceil(math.log2(INF))+1)
    s = [0] * length
    for _ in range(n):
        t,x = map(int,input().split())
        if t == 1:
            update(data,s,1,x,0,INF-1,1)
        else:
            left, right = 0, INF-1
            target = INF
            while left <= right:
                mid = (left+right) // 2
                if query(s,1,0,mid,0,INF-1) >= x:
                    target = mid
                    right = mid - 1
                else:
                    left = mid + 1
            print(target)
            update(data,s,1,target,0,INF-1,-1) 

def update(a,s,node,target,start,end,value):
    if start > target or end < target:
        return
    if start == end:
        a[end] += value; s[node] += value
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update(a,s,l_node,target,start,mid,value)
    update(a,s,r_node,target,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]

def query(s,node,left,right,start,end):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return query(s,l_node,left,right,start,mid) + query(s,r_node,left,right,mid+1,end)

if __name__ == '__main__':
    INF = 2000001
    main()