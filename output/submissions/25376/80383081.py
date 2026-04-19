from collections import deque

def main():
    print(solution(get_first_state(),get_switch(n),[-1] * (2 ** n)))

def get_first_state():
    array = list(map(int,input().split()))
    ret_value = 0
    for i in range(n):
        if array[i] == 1:
            ret_value += 2 ** i
    return ret_value

def get_switch(n):
    switch = [[] for _ in range(n)]
    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in tmp[1:]:
            switch[i].append(j-1)
    return switch

def solution(start,switch,visited):
    queue = deque([start])
    visited[start] = 0
    while queue:
        state = queue.popleft()
        for i in range(n):
            if state & 2 ** i != 0: continue
            next_state = get_next_state(switch,state,i)
            if visited[next_state] == -1:
                visited[next_state] = visited[state] + 1
                queue.append(next_state)
    return visited[2**n-1]

def get_next_state(switch,state,idx):
    state += 2 ** idx
    for i in switch[idx]:
        if state & 2 ** i == 0:
            state += 2 ** i
        else:
            state -= 2 ** i
    return state

if __name__ == "__main__":
    n = int(input())
    main()