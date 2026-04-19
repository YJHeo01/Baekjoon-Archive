from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    tmp = n * 15
    cut_off = tmp // 100
    if tmp % 100 >= 50:
        cut_off += 1
    array = []
    for _ in range(n):
        array.append(int(input()))
    queue = deque(sorted(array))
    for _ in range(cut_off):
        queue.popleft()
        queue.pop()
    tmp = 0
    while queue:
        tmp += queue.popleft()
    answer = tmp // (n-cut_off*2)
    if tmp % (n-cut_off*2) >= (n-cut_off) // 2:answer += 1
    if cut_off == 0: answer -= 1
    print(answer)
if __name__ == "__main__":
    main()