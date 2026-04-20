import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    answer = 0
    meet = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[1])
    before_meet = []
    after_meet = []
    start_prior = []
    for i in range(n):
        start, end = meet[i]
        start_prior.append((end-start,i))
        before_meet.append((start,end,i))
        after_meet.append((start,end,i))
    start_prior.sort()
    after_meet = sorted(after_meet,key=lambda x:x[1])
    before_meet = sorted(before_meet,key=lambda x:(-x[0],-x[1]))
    #print(meet)
    visited = [False] * n
    for _ in range(k):
        last_start, last_end = int(1e10),-1
        for i in range(n):
            tmp, idx = start_prior[i]
            if visited[idx] == False:
                last_start, last_end = meet[idx]
                answer += 1
                break
        if last_end == -1: break
        for i in range(n):
            start,end,idx = after_meet[i]
            if visited[idx] == False and start > last_end:
                answer += 1
                visited[idx] = True
                last_end = end
        for i in range(n):
            start,end,idx = before_meet[i]
            if visited[idx] == False and end < last_start:
                answer += 1
                visited[idx] = True
                last_start = start
        
    print(answer)

if __name__ == "__main__":
    main()