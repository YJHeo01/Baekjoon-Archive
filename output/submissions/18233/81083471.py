from itertools import combinations

def main():
    n,p,e = map(int,input().split())
    student = []
    for _ in range(n):
        student.append(list(map(int,input().split())))
    data = [0] * n
    for i in range(n): data[i] = i
    test_case_list = list(combinations(data,p))
    for test_case in test_case_list:
        min_value, max_value = 0,0
        for idx in test_case:
            min_value += student[idx][0]
            max_value += student[idx][1]
        if min_value > e or e > max_value: continue
        array = [0] * n
        for idx in test_case:
            array[idx] += student[idx][0]
            e -= student[idx][0]
        while True:
            if e == 0:
                break
            for idx in test_case:
                if array[idx] == student[idx][1]: continue
                tmp = min(student[idx][1]-array[idx],e)
                e -= tmp
                array[idx] += tmp
        print(*array)
        return
    print(-1)

if __name__ == "__main__":
    main()