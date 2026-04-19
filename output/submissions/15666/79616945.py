def main():
    array = list(map(int,input().split()))
    array.sort()
    backtracking(array,[],0)

def backtracking(array,answer,cur_idx):
    if len(answer) == m:
        print(*answer)
        return
    last_value = -1
    for i in range(cur_idx,n):
        if last_value != array[i]:
            last_value = array[i]
            backtracking(array,answer+[array[i]],i)
    return

if __name__  == "__main__":
    n,m = map(int,input().split())
    main()