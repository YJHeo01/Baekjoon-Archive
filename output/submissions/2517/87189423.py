import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    tmp = []
    for i in range(n):
        tmp.append((array[i],i))
    tmp.sort()
    s_length = 2 ** (math.ceil(math.log2(n)) + 1)
    leaf_node_start = s_length // 2 - 1
    for i in range(n):
        array[tmp[i][1]] = i
    s_length = 2 ** (math.ceil(math.log2(n)) + 1)
    s = [0] * s_length
    for i in range(n):
        rank = i + 1
        #print(array[i])
        print(rank - query(s,leaf_node_start,leaf_node_start+array[i]))
        update(s,leaf_node_start+array[i])

def query(s,start,end):
    ret_value = 0
    while start <= end:
        if start % 2 == 1:
            ret_value += s[start]
            start += 1
        if end % 2 == 0:
            #print(end)
            ret_value += s[end]
            end -= 1
        start = start // 2
        end = end // 2
    return ret_value

def update(s,node):
    while True:
        if node == 0: break
        s[node] += 1
        node = node // 2

if __name__ == "__main__":
    main()