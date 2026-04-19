import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted([list(map(int,input().split())) for _ in range(n)])
    answer = solution(array)
    print(answer)

def solution(array):
    l,p = map(int,input().split())
    array += [[l,0]]
    q = []
    cnt = 0
    for a,b in array:
        while True:
            if p >= a: break
            if q == []: return -1
            energy = heapq.heappop(q)
            cnt += 1
            p -= energy
        heapq.heappush(q,-b)
    
    return cnt
    

if __name__ == "__main__":
    main()