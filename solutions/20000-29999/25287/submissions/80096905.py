import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        print(solution(int(input()),list(map(int,input().split()))))

def solution(n,array):
    array[0] = min(array[0],n-array[0]+1)
    for idx in range(1,n):
        i = array[idx]
        new_value = n-i+1
        if min(i,new_value) >= array[idx-1]:
            array[idx] = min(i,new_value)
        elif max(i,new_value) >= array[idx-1]:
            array[idx] = max(i,new_value)
        else:
            return "NO"
    return "YES"

if __name__ == "__main__":
    main()