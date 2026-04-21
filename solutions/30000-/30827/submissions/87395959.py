import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    answer = 0
    meet = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[1])
    prior = []
    for i in range(n):
        prior.append((meet[i][1]-meet[i][0],i))
    #print(meet)
    visited = [False] * n
    for _ in range(k):
        last_start, last_end = int(1e10),-1
        for i in range(n):
            tmp, idx = prior[i]
            if visited[idx] == False:
                last_start, last_end = meet[idx]
                answer += 1
                break
        if last_end == -1: break
        for i in range(idx,n):
            if visited[i]: continue
            cur_start, cur_end = meet[i]
            if last_end < cur_start or cur_end < last_start:
                answer += 1
                visited[i] = True
                last_start = min(last_start,cur_start)
                last_end = max(last_end,cur_end)
        for i in range(idx-1,-1,-1):
            if visited[i]: continue
            cur_start, cur_end = meet[i]
            if last_end < cur_start or cur_end < last_start:
                answer += 1
                visited[i] = True
                last_start = min(last_start,cur_start)
                last_end = max(last_end,cur_end)            
    print(answer)

if __name__ == "__main__":
    main()