import sys

input = sys.stdin.readline

def main():
    n = int(input())
    print(solution(list(map(int,input().split())),[INF] * n))

def solution(array,LCS):
    answer = 0
    for value in array:
        target = answer
        left,right = 0,answer
        while left <= right:
            mid = (left+right) // 2
            if LCS[mid] >= value:
                right = mid - 1
                target = mid
            else:
                left = mid + 1
        LCS[target] = value
        if target == answer: answer += 1
    return answer

if __name__ == "__main__":
    INF = int(1e9) + 1
    main()