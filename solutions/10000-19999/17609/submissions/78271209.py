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
    while left <= right:
        left += 1; right -= 1
        if string[left] == string[right]: continue
        answer = min(pseudo_palindrome(string[left+1:right+1]),pseudo_palindrome(string[left:right]))
        break
    print(answer)

def pseudo_palindrome(string):
    left, right = 0,len(string)-1
    while left <= right:
        if string[left] != string[right]: return 2
        left += 1; right -= 1
    return 1

if __name__ == "__main__":
    main()