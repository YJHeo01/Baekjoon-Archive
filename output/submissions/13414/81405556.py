import sys, heapq

input = sys.stdin.readline

def main():
    k,l = map(int,input().split())
    information = {}
    for i in range(l):
        tmp = input().rstrip()
        information[tmp] = i
    q = []
    for id in information:
        heapq.heappush(q,(information[id],id))
    for _ in range(k):
        if q == []: break
        prior, id = heapq.heappop(q)
        print(id)

if __name__ == "__main__":
    main()