last_answer = []

def main():
    array = sorted(list(map(int,input().split())))
    solution(array,0,0,[])

def solution(array,cnt,idx,answer):
    if cnt == m:
        global last_answer
        if last_answer != answer:
            print(*answer)
            last_answer = answer
        return
    for next_idx in range(idx,n-m+cnt+1):
        solution(array,cnt+1,next_idx+1,answer+[array[next_idx]])

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()