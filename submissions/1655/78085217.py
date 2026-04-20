import heapq,sys

input = sys.stdin.readline

def main():
    mid_value = int(input())
    solution(mid_value)

def solution(mid_value):
    large_heap, small_heap = [], []
    print(mid_value)
    for i in range(1,n):
        tmp = int(input())
        if i % 2 != 0:
            if tmp > mid_value:
                heapq.heappush(large_heap,tmp)
            else:
                heapq.heappush(large_heap,mid_value)
                heapq.heappush(small_heap,-tmp)
                mid_value = -heapq.heappop(small_heap)
        else:
            if tmp < mid_value:
                heapq.heappush(small_heap,-tmp)
            else:
                heapq.heappush(small_heap,-mid_value)
                heapq.heappush(large_heap,tmp)
                mid_value = heapq.heappop(large_heap)
        print(mid_value)

if __name__ == "__main__":
    n = int(input())
    main()