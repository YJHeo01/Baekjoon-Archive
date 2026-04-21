import sys

input = sys.stdin.readline

def main():
    line = []
    for _ in range(n):
        a,b = map(int,input().split())
        if a > b: a,b = b,a
        line.append([a,b])
    length = int(input())
    line.sort()
    answer = 0
    answer = get_cnt(line,0,length)
    for i in range(1,n):
        if i > n - answer: break
        if line[i][1] - line[i][0] > length or line[i][0] == line[i-1][0]: continue
        answer = max(answer,get_cnt(line,i,length))
    print(answer)

def get_cnt(line,start,length):
    cnt = 0
    target = line[start][0] + length
    end = binary_search(line,start,length)
    for i in range(start,end+1):
        if line[i][1] <= target: cnt += 1
    return cnt

def binary_search(line,left,length):
    target = line[left][0] + length
    right = n-1
    ret_value = left
    while left <= right:
        mid = (left+right) // 2
        if line[mid][0] < target:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()