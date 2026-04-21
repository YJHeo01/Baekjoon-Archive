def main():
    n = int(input())
    print(solution(n,0))

def solution(value,cnt):
    if value == 1:
        return cnt
    ret_value = solution(value-1,cnt+1)
    if value % 3 == 0:
        ret_value = min(ret_value,solution(value//3,cnt+1))
    if value % 2 == 0:
        ret_value = min(ret_value,solution(value//2,cnt+1))
    return ret_value

if __name__ == "__main__":
    main()