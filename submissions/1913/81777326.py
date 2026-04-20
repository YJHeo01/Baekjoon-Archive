def main():
    n = int(input())
    target = int(input())
    array = [[1]*n for _ in range(n)]
    answer = solution(array,target,n)
    for row in array:
        print(*row)
    print(*answer)

def solution(array,target,n):
    value = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    move_idx = 0
    move_cnt = 1
    vx,vy = n // 2, n // 2
    ret_value = (n//2+1,n//2+1)
    while True:
        for _ in range(2):
            for _ in range(move_cnt):
                value += 1
                if value > n ** 2: return ret_value
                vx += dx[move_idx]
                vy += dy[move_idx]
                array[vx][vy] = value
                if value == target: ret_value = (vx+1,vy+1)
            move_idx += 1
            move_idx %= 4
        move_cnt += 1

if __name__ == "__main__":
    main()