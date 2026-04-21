from collections import deque
import sys

sys.setrecursionlimit(10**6)

def main():
    global n
    tc = int(input())
    while True:
        if tc == 0:
            break
        n = int(input())
        solution(1,2,[],1)
        print()
        tc -= 1

def solution(sum_value,value,command,last_value):
    if value > n:
        if sum_value == 0:
            print_answer(command)
        return
    if last_value > 0:
        solution(sum_value+last_value*9+value,value+1,command + [' '],last_value*10+value)
    else:
        solution(sum_value+last_value*9-value,value+1,command + [' '],last_value*10-value)
    solution(sum_value+value,value+1,command + ['+'],value)
    solution(sum_value-value,value+1,command + ['-'],-value)

def print_answer(queue):
    value = 1
    queue = deque(queue)
    while True:
        print(value,end="")
        if queue == deque([]):
            print()
            break
        command = queue.popleft()
        print(command,end="")
        value += 1
    
if __name__ == "__main__":
    main()