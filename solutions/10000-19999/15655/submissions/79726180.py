def main():
    array = list(map(int,input().split()))
    array.sort()
    backtracking(array,[],-1)

def backtracking(array,answer,end_idx):
    if len(answer) == m:
        print(*answer)
        return
    last_value = -1
    for i in range(end_idx+1,n):
        if array[i] != last_value:
            last_value = array[i]
            backtracking(array,answer+[array[i]],i)

if __name__  == "__main__":
    n,m = map(int,input().split())
    main()