import sys,heapq

input = sys.stdin.readline

def main():
    n = int(input())
    visited = [False] * 10001
    possible_day = [0] * (10001)
    for i in range(10001):
        possible_day[i] = i
    q = []
    for _ in range(n):
        a,b = map(int,input().split())
        heapq.heappush(q,(-a,b))
    answer = 0
    while q:
        p,d = heapq.heappop(q)
        if possible_day[d] == 0: continue
        day = possible_day[d]
        while True:
            if day == 0:break
            if visited[day] == False:
                visited[day] = True
                possible_day[d] = day - 1
                answer -= p
                break
            day -= 1
    print(answer)

if __name__  == "__main__":
    main()