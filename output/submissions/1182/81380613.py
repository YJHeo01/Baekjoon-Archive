def main():
    array = list(map(int,input().split()))
    answer = backtracking(array,s,0,0)
    print(answer)

def backtracking(array,target,start_idx,value):
    if target == value: return 1
    if start_idx == n: return 0
    for i in range(start_idx,n):
        ret_value += backtracking(array,target,i+1,value+array[i])
    return ret_value

if __name__ == "__main__":
    n,s = map(int,input().split())
    main()