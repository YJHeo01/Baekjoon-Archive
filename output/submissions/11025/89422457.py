import sys, math

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    s_length = 2 ** math.ceil(math.log2(n)+1)
    s = [0] * s_length
    leaf_node_start = s_length // 2
    for i in range(n):
        s[leaf_node_start+i] = 1
    #print(s)
    init(s,s_length-1)
    cnt = n
    #print(s)
    answer = -1
    start = 0
    for i in range(n):
        left, right = start, n-1
        answer = n
        target = k
        while left <= right:
            mid = (left+right) // 2
            tmp = query(s,leaf_node_start+start,leaf_node_start+mid)
            if tmp >= target:
                if s[leaf_node_start+mid] != 0:
                    answer = mid
                right = mid - 1
            else:
                left = mid + 1
        if answer == n:
            target = k - query(s,leaf_node_start+start,s_length-1)
            target -= target // cnt * cnt
            if target == 0: target += cnt
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) // 2
                tmp = query(s,leaf_node_start,leaf_node_start+mid)
                if tmp >= target:
                    if s[leaf_node_start+mid] != 0:
                        answer = mid
                    right = mid - 1
                else:
                    left = mid + 1
        update(s,leaf_node_start+answer)
        cnt -= 1
        start = answer
    print(answer+1)

def init(s,node):
    while True:
        if node == 1: break
        s[node//2] += s[node]
        node -= 1

def query(s,start,end):
    ret_value = 0
    while start <= end:
        if start % 2 == 1:
            ret_value += s[start]
            start += 1
        if end % 2 == 0:
            ret_value += s[end]
            end -= 1
        start = start // 2
        end = end // 2
    return ret_value

def update(s,node):
    while True:
        if node == 0: break
        s[node] -= 1
        node = node // 2

if __name__ == "__main__":
    main()