import sys

input = sys.stdin.readline

def main():
    global k
    n,m,k,s,T = map(int,input().split())
    ski = [[] for _ in range(n+1)]
    lift = []
    for _ in range(m):
        a,b,t = map(int,input().split())
        ski[a].append((b,t))
        lift.append((b,a))
    time = [[-1]*(k+1) for _ in range(n+1)]
    time[s][0] = 0
    for cnt in range(k+1):
        for a in range(1,n+1):
            if time[a][cnt] == -1: continue
            for b,t in ski[a]:
                time[b][cnt] = max(time[b][cnt],time[a][cnt]+t)
        if cnt == k: break
        for b,a in lift:
            time[a][cnt+1] = max(time[a][cnt+1],time[b][cnt])
    print(max(time[T]))

if __name__ == "__main__":
    main()