def main():
    answer = -1
    n,t = map(int,input().split())
    for _ in range(n):
        s,i,c = map(int,input().split())
        for x in range(c):
            if s + i * x < t: continue
            time = s + i * x - t
            if answer == -1:answer = time
            else:
                answer = min(answer,time)
    print(answer)

if __name__  == "__main__":
    main()