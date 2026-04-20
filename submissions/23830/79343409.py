def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    p,q,r,s = map(int,input().split())
    init_score_sum = sum(array)
    answer = -1
    for k in range(1,100002):
        left, right = 0,n-1
        target = -1
        score_sum = init_score_sum
        while left <= right:
            mid = (left+right) // 2
            if array[mid] < k:
                target = mid
                left = mid + 1
            else:
                right = mid - 1
        score_sum += ((target+1) * q)
        left, right = 0,n-1
        target = n
        while left <= right:
            mid = (left+right) // 2
            if array[mid] > k + r:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        score_sum -= ((n-target)*p)
        if score_sum >= s:
            answer = k
            break
    print(answer)