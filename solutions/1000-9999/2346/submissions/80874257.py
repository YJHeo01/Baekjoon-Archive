import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    visited = [False] * n
    idx = 0
    answer = [1]
    for _ in range(n-1):
        visited[idx] = True
        if array[idx] > 0:
            dx = 1
            movement = array[idx]
        else:
            dx = -1
            movement = -array[idx]
        move_cnt = 0
        while True:
            idx += dx
            idx %= n
            if visited[idx] == True: continue
            move_cnt += 1
            if move_cnt == movement: break
        answer.append(idx+1)
    print(*answer)

if __name__ == "__main__":
    main()