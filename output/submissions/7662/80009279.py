import sys, heapq

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    k = int(input())
    idx = -1
    visited = []
    max_heap, min_heap = [], []
    for _ in range(k):
        command, value = input().split()
        value = int(value)
        if command == 'I':
            idx += 1
            visited.append(False)
            heapq.heappush(min_heap,(value,idx))
            heapq.heappush(max_heap,(-value,idx))
        else:
            if value == -1:
                while True:
                    if min_heap == []:
                        break
                    data, idx = heapq.heappop(min_heap)
                    if visited[idx] == True: continue
                    visited[idx] = True
                    break
            else:
                while True:
                    if max_heap == []:
                        break
                    data, idx = heapq.heappop(max_heap)
                    if visited[idx] == True:
                        continue
                    visited[idx] = True
                    break
    print_answer(max_heap,min_heap,visited)
    
def print_answer(max_heap,min_heap,visited):
    while True:
        if max_heap == []:
            print("EMPTY")
            return
        value, idx = heapq.heappop(max_heap)
        if visited[idx] == False:
            print(-value,end=" ")
            break
    while True:
        value, idx = heapq.heappop(min_heap)
        if visited[idx] == False:
            print(value)
            break
if __name__ == "__main__":
    main()