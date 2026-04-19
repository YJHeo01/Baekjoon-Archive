import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    array = []
    for _ in range(n):
        array.append(int(input()))
    s = [0] * s_length
    answer = 0
    init(array,s,1,0,n-1)
    for left in range(n):
        for right in range(left,n):
            answer = max(answer,(right-left+1)*query(s,1,left,right,0,n-1))
    print(answer)

def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    init(a,s,node*2,start,mid(start,end))
    init(a,s,node*2+1,mid(start,end)+1,end)
    s[node] = min(s[node*2],s[node*2+1])

def mid(start,end):
    return (start+end) // 2

def query(s,node,left,right,start,end):
    if start > right or end < left:
        return INF
    if left <= start and end <= right:
        return s[node]
    return min(query(s,node*2,left,right,start,mid(start,end)),query(s,node*2+1,left,right,mid(start,end)+1,end))

if __name__ == "__main__":
    INF = int(1e9)
    main()