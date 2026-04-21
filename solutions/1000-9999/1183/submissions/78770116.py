def main():
    n = int(input())
    t = INF
    arrive_time = []
    for _ in range(n):
        a,b = map(int,input().split())
        arrive_time.append((a,b))
        t = min(t,(b-a))
    answer = 1
    best_wait_time = INF
    while True:
        wait_time = 0
        for wizard, muggle in arrive_time:
            wait_time += abs(wizard+t-muggle)
        if wait_time > best_wait_time:
            break
        elif best_wait_time > wait_time:
            answer = 1
            best_wait_time = wait_time
        else:
            answer += 1
        t += 1
    print(answer)

if __name__ == "__main__":
    INF = int(1e11)
    main()