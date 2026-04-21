n = int(input())
heap = [0]*(n+1)
global last_i

last_i = 0

def heap_pop():
    global last_i
    if last_i == 0:
        return 0
    ret_val = heap[1]
    heap[1] = heap[last_i]
    last_i -= 1
    cur_i = 1
    while 1:
        left = cur_i * 2
        right = left + 1
        smallest = cur_i
        if left <= last_i and heap[left] < heap[smallest]:
            smallest = left
        if right <= last_i and heap[right] < heap[smallest]:
            smallest = right
        if smallest == cur_i:
            return ret_val
        heap[smallest], heap[cur_i] = heap[cur_i], heap[smallest]
        cur_i = smallest
def heap_push(x):
    global last_i
    last_i += 1
    heap[last_i] = x
    cur_i = last_i
    parent_i = cur_i // 2
    while parent_i >= 1:
        if heap[parent_i] < heap[cur_i]:
            return
        heap[parent_i], heap[cur_i] = heap[cur_i], heap[parent_i]
        cur_i = parent_i
        parent_i = parent_i//2
for i in range(n):
    x = int(input())
    if x == 0:
        v = heap_pop()
        print(v)
    else:
        heap_push(x)
