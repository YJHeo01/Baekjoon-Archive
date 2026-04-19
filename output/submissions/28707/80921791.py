import sys, heapq

input = sys.stdin.readline

def main():
    INF = int(1e9)
    n = int(input())
    array = list(map(int,input().split()))
    m = int(input())
    command = []
    for _ in range(m):
        l,r,c = map(int,input().split())
        command.append((c,l-1,r-1))
    command.sort()
    cost_list = {}
    answer = INF
    solution(command,cost_list,array)
    for cost in cost_list:
        correnct = True
        for i in range(1,n):
            if int(cost[i]) < int(cost[i-1]):
                correnct = False
                break
        if correnct == True:
            answer = min(answer,cost_list[cost])
    if answer >= INF: answer = -1
    print(answer)

def solution(command,cost_list,array):
    start = ""
    for i in array:
        start += str(i-1)
    q = [(0,start)]
    cost_list[start] = 0
    while q:
        cost, vx = heapq.heappop(q)
        if cost > cost_list[vx]: continue
        for c,a,b in command:
            nx = vx[:a] + vx[b] + vx[a+1:b] + vx[a] + vx[b+1:]
            if nx not in cost_list or cost_list[nx] > cost + c:
                cost_list[nx] = cost + c
                heapq.heappush(q,(cost_list[nx],nx))

if __name__ == "__main__":
    main()