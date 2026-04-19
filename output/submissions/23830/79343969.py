def main():
    n = int(input())
    student = list(map(int,input().split()))
    student.sort()
    p,q,r,s = map(int,input().split())
    init_score_sum = sum(student)
    answer = -1
    for k in range(1,100002):
        left, right = 0,n-1
        plus_cnt = -1
        score_sum = init_score_sum
        while left <= right:
            mid = (left+right) // 2
            if student[mid] >= k:
                plus_cnt = mid
                right = mid - 1
            else:
                left = mid + 1
        score_sum += (plus_cnt * q)
        if score_sum < s:continue
        left, right = 0,n-1
        minus_cnt = n
        while left <= right:
            mid = (left+right) // 2
            if student[mid] > k + r:
                minus_cnt = mid
                right = mid - 1
            else:
                left = mid + 1
        minus_cnt = n - minus_cnt
        score_sum -= p * minus_cnt
        if score_sum >= s:
            answer = k
            break
    print(answer)

if __name__ == "__main__":
    main()