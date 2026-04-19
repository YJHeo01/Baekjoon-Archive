from collections import deque

def main():
    n,k,t = map(int,input().split())
    array = deque(sorted(list(map(int,input().split()))))
    print(solution(array,k,t))

def solution(q,k,t):
    stack = []
    while q:
        value = q.popleft()
        if value >= t:
            while stack:
                t += stack.pop()
                k -= 1
                if k == 0 or t > value: break
        if value >= t or k == 0: break
        stack.append(value)
    for _ in range(min(k,len(stack))):
        t += stack.pop()
    return t

if __name__ == "__main__":
    main()