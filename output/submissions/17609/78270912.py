import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    string = list(input())
    left, right = -1,len(string) -1
    answer = 0
    while left < right:
        left += 1; right -= 1
        if string[left] == string[right]: continue
        if answer == 1: answer = 2; break
        answer = 1
        if string[left+1] == string[right]: left += 1
        elif string[left] == string[right-1]: right -= 1
        else: answer = 2; break
    if answer >= 2: answer = 2
    print(answer)
        
if __name__ == "__main__":
    main()