import sys, heapq

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    k = int(input())
    _idx = -1
    erase = []
    max_heap, min_heap = [], []
    for _ in range(k):
        command, value = input().split()
        value = int(value)
        if command == 'I':
            _idx += 1
            erase.append(False)
            heapq.heappush(min_heap,(value,_idx))
            heapq.heappush(max_heap,(-value,_idx))
        else:
            if value == -1:
                delete_value(min_heap,erase)
            else:
                delete_value(max_heap,erase)

    print_answer(max_heap,min_heap,erase)

def delete_value(heap,erase):
    while True:
        if heap == []:
            break
        data, idx = heapq.heappop(heap)
        if erase[idx] == True:
            continue
        erase[idx] = True
        return

def print_answer(max_heap,min_heap,erase):
    while True:
        if max_heap == []:
            print("EMPTY")
            return
        value, idx = heapq.heappop(max_heap)
        if erase[idx] == False:
            print(-value,end=" ")
            break
    while True:
        value, idx = heapq.heappop(min_heap)
        if erase[idx] == False:
            print(value)
            break

if __name__ == "__main__":
    main()