import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_size = 2 ** (math.ceil(math.log2(n))+1)
    s = [0] * s_size
    set_s(array,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        c,i,j = map(int,input().split())
        if c == 1:
            array[i-1] = j
            set_s(array,s,1,0,n-1)
        else:
            answer = query(array,s,1,i-1,j-1,0,n-1) + 1
            print(answer)

def set_s(array,s,node,start,end):
    if start == end:
        s[node] = start
        return start
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    set_s(array,s,l_node,start,mid)
    set_s(array,s,r_node,mid+1,end)
    ret_value = l_node
    if array[s[l_node]] > array[s[r_node]]:
        s[node] = s[node*2+1]
        ret_value = r_node
    else:
        s[node] = s[node*2]
    return ret_value

def query(array,s,node,left,right,start,end):
    if start >= right: return right
    if end <= left: return left
    if left <= start and end <= right: return s[node]
    l_node = 2 * node; r_node = l_node + 1
    mid = (start+end) // 2
    l_min = query(array,s,l_node,left,right,start,mid)
    r_min = query(array,s,r_node,left,right,mid+1,end)
    if array[l_min] > array[r_min]: return r_min
    else: return l_min

if __name__ == "__main__":
    main()