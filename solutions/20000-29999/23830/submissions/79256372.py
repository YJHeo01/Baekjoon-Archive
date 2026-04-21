def main():
    n = int(input())
    student = list(map(int,input().split()))
    student.sort()
    init_score = sum(student)
    p,q,r,s = map(int,input().split())
    if init_score >= s:
        print(0)
        return
    answer = -1
    k_left, k_right = 0,max(student)
    while k_left <= k_right:
        k = (k_left+k_right) // 2
        student_L, student_R = 0, n-1
        plus_cnt = 0
        while student_L <= student_R:
            mid = (student_L+student_R) // 2
            if student[mid] >= k:
                plus_cnt = mid
                student_R = mid - 1
            else:
                student_L = mid + 1
        student_L, student_R, minus_cnt = 0, n-1, 0
        while student_L <= student_R:
            mid = (student_L+student_R) // 2
            if student[mid] > k + r:
                minus_cnt = mid
                student_R = mid - 1
            else:
                student_L = mid + 1
        minus_cnt = n - minus_cnt
        tmp_score = init_score + plus_cnt * q - minus_cnt * p
        if tmp_score >= s:
            answer = k
            k_right = k - 1
        else:
            k_left = k + 1
    print(answer)

if __name__ == "__main__":
    main()