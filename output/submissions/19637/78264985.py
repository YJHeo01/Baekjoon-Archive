import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    title_list = get_title_list(n)
    solution(title_list,m)

def get_title_list(n):
    ret_value = []
    last_power = -1
    for _ in range(n):
        title, power = input().split()
        power = int(power)
        if power <= last_power: continue
        ret_value.append((title,power))
        last_power = power
    return ret_value

def solution(title_list,m):
    right = len(title_list) - 1 
    for _ in range(m):
        value = int(input())
        answer = get_answer(title_list,value,right)
        print(answer)

def get_answer(title_list,value,right):
    answer = title_list[right][1]
    left = 0
    while left <= right:
        mid = (left+right) // 2
        if title_list[mid][1] >= value:
            answer = title_list[mid][0]
            right = mid - 1    
        else:
            left = mid + 1
    return answer

if __name__ == "__main__":
    main()