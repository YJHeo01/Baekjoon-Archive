def main():
    n,k = map(int,input().split())
    print(solution(n,k))

def solution(n,k):
    idx = 0
    erase = [False] * (n+1)
    for i in range(2,n+1):
        if erase[i] == True: continue
        for j in range(i,n+1,i):
            if erase[j] == True: continue
            erase[j] = True
            idx += 1
            if k == idx: return j

if __name__ == "__main__":
    main()