from collections import deque
import sys

input = sys.stdin.readline

def main():
    cost = [int(input()) for _ in range(n)]
    use = [False] * n
    car_weight = [int(input()) for _ in range(m)]
    car_position = [-1] * m
    wait = deque([])
    
    for _ in range(2*m):
        i = int(input())
        if i > 0:
            i -= 1
            car_in(wait,use,car_position,i)
        else:
            i *= -1; i -= 1
            car_out(wait,use,car_position,i)
    
    answer = 0
    
    for i in range(m):
        answer += car_weight[i] * cost[car_position[i]]
    
    print(answer)

def car_in(wait,use,car_position,i):
    if wait != deque([]):
        wait.append(i)
        return
    for j in range(n):
        if use[j] == False:
            use[j] = True
            car_position[i] = j
            return
    wait.append(i)

def car_out(wait,use,car_position,i):
    if wait == deque([]):
        use[car_position[i]] = False
        return
    next_car = wait.popleft()
    car_position[next_car] = car_position[i]

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()