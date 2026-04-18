import sys, math
import bisect
input = sys.stdin.readline

def main():
    INF = int(1e9)
    array = list(map(int,input().split()))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    s = [[] for _ in range(s_length+1)]
    init(array,s,1,0,n-1)
    for i in range(1,s_length+1):
        s[i].sort()
    ans = []
    for _ in range(m):
        i,j,k = map(int,input().split())
        target = INF
        left, right = -INF, INF
        while left <= right:
            mid = (left+right)//2
            tmp = query(s,1,i-1,j-1,0,n-1,mid)
            if tmp >= k:
                right = mid - 1
                target = mid
            else:
                left = mid + 1
        ans.append(target)
    sys.stdout.write('\n'.join(map(str,ans)))

def init(a,s,node,start,end):
    s[node] = sorted(a[start:end+1])
    if start != end:
        mid = (start+end) // 2
        init(a,s,node*2,start,mid)
        init(a,s,node*2+1,mid+1,end)
    

def query(s,node,left,right,start,end,k):
    if start > right or left > end: return 0
    elif left <= start and end <= right:
        return bisect.bisect_right(s[node], k)
    else:
        return query(s,node*2,left,right,start,(start+end)//2,k) + query(s,node*2+1,left,right,(start+end)//2+1,end,k)

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()