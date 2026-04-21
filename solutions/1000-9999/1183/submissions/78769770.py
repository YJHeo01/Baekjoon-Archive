def main():
    n = int(input())
    max_value, min_value = -INF, INF
    arrive_time = []
    for _ in range(n):
        a,b = map(int,input().split())
        value = b - a
        arrive_time.append((a,b))
        max_value = max(max_value,value)
        min_value = min(min_value,value)
    answer = 0
    best_wait_time = INF
    for t in range(min_value,max_value+1):
        wait_time = 0
        for wizard,muggle in arrive_time:
            wait_time += abs(wizard + t - muggle)
        if wait_time < best_wait_time:
            answer = 1
            best_wait_time = wait_time
        elif wait_time == best_wait_time: answer += 1
        
    print(answer)

if __name__ == "__main__":
    INF = int(1e9)
    main()