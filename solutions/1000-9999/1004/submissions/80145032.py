def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    start_end = list(map(int,input().split()))
    n = int(input())
    answer = 0
    for _ in range(n):
        x,y,r = map(int,input().split())
        state = 0
        for i in range(2):
            target_x, target_y = start_end[2*i], start_end[2*i+1]
            if (target_x-x) ** 2 + (target_y-y) ** 2 <= r**2:
                state += 1    
        if state == 1:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()