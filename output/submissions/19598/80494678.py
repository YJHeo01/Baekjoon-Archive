import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    
    for _ in range(n):
        array.append(list(map(int,input().split())))
    
    array.sort()
    answer, tmp = 0,0
    q = []
    
    for start,end in array:
        while q:
            last_end = heapq.heappop(q)
            if last_end > start:
                heapq.heappush(q,last_end)
                break
            tmp -= 1
        tmp += 1
        heapq.heappush(q,end)
        answer = max(answer,tmp)
    
    print(answer)
        
if __name__ == "__main__":
    main()