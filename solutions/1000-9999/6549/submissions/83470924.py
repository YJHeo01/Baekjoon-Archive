import sys

input = sys.stdin.readline

def main():
    while True:
        array = list(map(int,input().split()))
        if array[0] == 0: return
        n, array = array[0], array[1:]
        solution(array,n)

def solution(array,n):
    stack = []
    answer = 0
    
    for next_idx in range(n):
        idx = next_idx
        while stack:
            height, cur_idx = stack.pop()
            if array[next_idx] >= height:
                stack.append((height,cur_idx))
                break
            idx = min(idx,cur_idx)
            answer = max(answer,height*(next_idx-cur_idx))
        stack.append((array[next_idx],idx))
    
    while stack:
        height, idx = stack.pop()
        answer = max(answer,height*(n-idx))
    
    print(answer)

if __name__ == "__main__":
    main()