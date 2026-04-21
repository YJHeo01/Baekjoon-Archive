import sys,math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_size = 2 ** (math.ceil(math.log2(n)) + 1)
    s = [0] * s_size
    m = int(input())
    for _ in range(m):
        command = list(map(int,input().split()))
        if command[0] == 1: update(s,1,command[1]-1,command[2]-1,0,n-1,command[3])
        else: print(array[command[1]-1] + query(s,1,command[1]-1,0,n-1))

def update(s,node,left,right,start,end,value):
    if end < left or start > right: return
    if left <= start and end <= right:
        s[node] += value
        return
    l_node = node * 2; r_node = l_node + 1; mid = (start+end) // 2
    update(s,l_node,left,right,start,mid,value)
    update(s,r_node,left,right,mid+1,end,value)

def query(s,node,target,start,end):
    if start > target or end < target: return 0
    if start == end: return s[node]
    l_node = node * 2; r_node = l_node + 1; mid = (start+end) // 2
    return s[node] + query(s,l_node,target,start,mid) + query(s,r_node,target,mid+1,end)

if __name__ == "__main__":
    main()