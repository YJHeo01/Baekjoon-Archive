import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    cnt = [0] * 1000001
    s = [0] * (2 ** (math.ceil(math.log2(INF))+1))
    for _ in range(n):
        a, *tmp = input().split()
        if a == '1':
            b = int(tmp[0])
            left, right = 0, INF
            target = INF
            while left <= right:
                mid = (left+right) // 2
                value = query(s,1,1,mid,1,INF-1)
                if value >= b:
                    right = mid - 1
                    target = mid
                else:
                    left = mid + 1    
            print(target)
            update(cnt,s,1,target,1,INF-1,-1)
        else:
            b,c = tmp
            update(cnt,s,1,int(b),1,INF-1,int(c))

def query(s,node,left,right,start,end):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return s[node]
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    return query(s,l_node,left,right,start,mid) + query(s,r_node,left,right,mid+1,end)

def update(a,s,node,target,start,end,value):
    if start > target or end < target:
        return
    if start == end and target == end:
        a[end] += value; s[node] += value
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    update(a,s,l_node,target,start,mid,value)
    update(a,s,r_node,target,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]

if __name__ == '__main__':
    INF = 1000001
    main()