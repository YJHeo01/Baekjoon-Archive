from collections import deque

def main():
    n,k = map(int,input().split())
    queue = deque([])
    visited = [False] * (n+1)
    idx = 0
    line_up = 1
    cnt = 0
    while True:
        idx += 1
        if idx > n: idx = 1
        if visited[idx] == True:
            continue
        if line_up == k:
            visited[idx] = True
            line_up = 0
            queue.append(idx)
            cnt += 1
        if cnt == n:
            break
        line_up += 1
    print_answer(queue)
    
def print_answer(queue):
    print("<",end="")
    while True:
        print(queue.popleft(),end="")
        if queue == deque([]):
            break
        print(",",end=" ")
    print(">")

if __name__ == "__main__":
    main()