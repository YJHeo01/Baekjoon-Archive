import math

def main():
    n = int(input())
    num_list = []
    for i in range(1,100001):
        num_list.append(i**2)
    answer = 0
    length = len(num_list)
    target_idx = length - 1
    left, right = 0,target_idx
    while left <= right:
        mid = (left+right) // 2
        if num_list[mid] >= n:
            target_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    if num_list[target_idx] == n:
        print(-1)
        return
    left, right = 0, target_idx-1
    while left < right:
        if num_list[left] + num_list[right] > n:
            right -= 1
        elif num_list[left] + num_list[right] < n:
            left += 1
        else:
            answer += 1
            right -= 1; left += 1
    for i in range(1,int(math.sqrt(n))+1):
        if n % i != 0: continue
        if ((i+(n//i))%2 == 0 and i != n // i): answer += 1
    print(answer)

if __name__ == "__main__":
    main()