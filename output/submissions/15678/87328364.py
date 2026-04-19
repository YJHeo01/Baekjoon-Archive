#중복해서 다리를 밟을 수 없음, u v의 차이가 d이하 -> 작은 수부터 큰 수 순서로 진행해준다.
# 처음에 든 생각 : 데이크스트라 but) 그래프로 생각할 경우 엣지의 수가 (10**5+1) * (10**5 // 2)이므로 TLE
# 두 번째로 든 생각 : 2차원 배열 dp but) 이도 TLE나 메모리 초과 발생 가능생 생각
# 세 번째로 든 생각 : 세그먼트 트리

import sys, math

input = sys.stdin.readline

def main():
    global n
    n,d = map(int,input().split())
    array = list(map(int,input().split()))
    s_length = 2 ** math.ceil(math.log2(n)+1)
    s = [-INF] * s_length
    leaf_node_start = s_length // 2 - 1
    answer = -INF
    for i in range(n):
        tmp = max(0,query(s,leaf_node_start+max(0,i-d),leaf_node_start+max(1,i)-1)) + array[i]
        answer = max(answer,tmp)
        s[leaf_node_start+i] = tmp
        update(s,leaf_node_start+i)
    print(answer)

def query(s,start,end):
    ret_value = -INF
    while start <= end:
        if start % 2 == 1:
            ret_value = max(ret_value,s[start])
            start += 1
        if end % 2 == 0:
            ret_value = max(ret_value,s[end])
            end -= 1
        start = start // 2
        end = end // 2
    return ret_value

def update(s,node):
    while True:
        node = node // 2
        if node == 0: break
        s[node] = max(s[node*2],s[node*2+1])

if __name__ == "__main__":
    INF = int(1e15)
    main()