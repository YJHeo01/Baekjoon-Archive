def main():
    t = int(input())
    for _ in range(t):
        m,n,x,y = map(int,input().split())
        answer = solution(m,n,x,y)
        print(answer)

def solution(m,n,target_x,target_y):
    x, y = 1,1
    idx = 1
    while True:
        if x == target_x and y == target_y:
            break
        x = get_next_value(m,x)
        y = get_next_value(n,y)
        idx += 1
        if idx > m*n: return -1
    return idx

def get_next_value(limit,value):
    if value < limit: return value + 1
    else: return 1

if __name__ == "__main__":
    main()