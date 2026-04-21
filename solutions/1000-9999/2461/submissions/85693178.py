import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = [sorted(list(map(int,input().split()))) for _ in range(n)]
    pnt_list = [0] * n #n개의 포인터로 관리
    min_value_idx, max_value_idx = 0,0
    answer = int(1e9)
    while True:
        for i in range(n):
            if array[min_value_idx][pnt_list[min_value_idx]] > array[i][pnt_list[i]]:
                min_value_idx = i
            elif array[min_value_idx][pnt_list[min_value_idx]] == array[i][pnt_list[i]]:
                if pnt_list[min_value_idx] + 1 == m or pnt_list[i] + 1 == m:
                    continue
                if array[min_value_idx][pnt_list[min_value_idx] + 1] > array[i][pnt_list[i]+1]:
                    min_value_idx = i
            if array[i][pnt_list[i]] > array[max_value_idx][pnt_list[max_value_idx]]:
                max_value_idx = i
        answer = min(answer,array[max_value_idx][pnt_list[max_value_idx]]-array[min_value_idx][pnt_list[min_value_idx]])
        pnt_list[min_value_idx] += 1
        if pnt_list[min_value_idx] == m: break
    print(answer)

if __name__ == "__main__":
    main()