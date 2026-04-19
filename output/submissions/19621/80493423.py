input = sys.stdin.readline

def main():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    array.sort()
    answer = backtracking(array,0,0,-1)
    print(answer)

def backtracking(array,start,cnt,last_finish_time):
    ret_value = cnt
    for i in range(start,n):
        if last_finish_time > array[i][0]: continue
        ret_value = max(ret_value,backtracking(array,i+1,cnt+array[i][2],array[i][1]))
    return ret_value


if __name__ == "__main__":
    n = int(input())
    main()