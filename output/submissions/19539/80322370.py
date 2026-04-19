import heapq, sys

input = sys.stdin.readline

def main():
    n = int(input())
    q = list(map(int,input().split()))
    for i in range(n):
        q[i] *= -1
    heapq.heapify(q)
    answer = 'YES'
    while True:
        if q == [] or answer != 'YES':
            break
        for i in range(2,0,-1):
            if q == []:
                answer = 'NO'
                break
            value = heapq.heappop(q)
            if value == 0 and i == 2:break
            value += i
            if value < 0:
                heapq.heappush(q,value)
            elif value > 0:
                answer = 'NO'
    print(answer)

if __name__ == "__main__":
    main()