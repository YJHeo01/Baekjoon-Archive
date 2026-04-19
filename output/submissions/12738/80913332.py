def main():
    print(solution(list(map(int,input().split())),[INF] * n))

def solution(array,LCS):
    answer = 0
    for i in range(n):
        value = array[i]
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
    n = int(input())
    INF = int(1e9) + 1
    main()