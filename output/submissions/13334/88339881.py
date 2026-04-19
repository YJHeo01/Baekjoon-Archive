import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    for _ in range(n):
        l,r = map(int,input().split())
        if l > r: l,r = r,l
        array.append((l,r))
    array.sort(key=lambda x:x[1])
    d = int(input())
    q = []
    answer = 0
    cnt = 0
    for l,r in array:
        if l + d < r: continue
        cnt += 1
        heapq.heappush(q,l)
        while q:
            tmp = heapq.heappop(q)
            if tmp >= r - d:
                heapq.heappush(q,tmp)
                break
            else:
                cnt -= 1
        answer = max(answer,cnt)
    print(answer)
        
if __name__ == "__main__":
    main()