import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    tmp = sorted(array)
    dic = {}
    #print(tmp)
    for i in range(n):
        dic[tmp[i]] = i
    for i in range(n):
        array[i] = dic[array[i]]
    a = [0] * n
    s_length = 2 ** (math.ceil(math.log2(n)) + 1)
    s = [0] * s_length
    for i in range(n):
        rank = i + 1
        print(rank - query(s,1,array[i],0,n-1))
        update(a,s,1,array[i],0,n-1)

def query(s,node,target,start,end):
    if start > target: return 0
    if end <= target: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return query(s,l_node,target,start,mid) + query(s,r_node,target,mid+1,end)

def update(a,s,node,target,start,end):
    if start > target or end < target: return
    if start == end:
        a[end] += 1
        s[node] += 1
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    update(a,s,l_node,target,start,mid)
    update(a,s,r_node,target,mid+1,end)
    s[node] = s[l_node] + s[r_node]

if __name__ == "__main__":
    main()