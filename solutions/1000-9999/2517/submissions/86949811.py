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
    s_length = 2 ** (math.ceil(math.log2(n)) + 1)
    s = [0] * s_length
    print(1)
    update(s,1,array[0],0,n-1)
    rank = 1
    for i in range(1,n):
        rank += 1
        if array[i] > array[i-1]:
            rank -= query(s,1,array[i-1],array[i],0,n-1)
        else:
            rank += query(s,1,array[i],array[i-1],0,n-1)
            rank -= 1
        print(rank)
        update(s,1,array[i],0,n-1)

def query(s,node,left,right,start,end):
    if end < left or start > right or s[node] == 0: return 0
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return query(s,l_node,left,right,start,mid) + query(s,r_node,left,right,mid+1,end)

def update(s,node,target,start,end):
    if start > target or end < target: return s[node]
    if start == end:
        s[node] += 1
        return s[node]
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    s[node] = update(s,l_node,target,start,mid) + update(s,r_node,target,mid+1,end)
    return s[node]

if __name__ == "__main__":
    main()