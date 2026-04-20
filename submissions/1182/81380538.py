def main():
    array = list(map(int,input().split()))
    array.sort()
    answer = backtracking(array,s,0,0)
    print(answer)

def backtracking(array,target,start_idx,value):
    if start_idx == n: return 0
    ret_value = 0
    for i in range(start_idx,n):
        if value + array[i] > target:
            return ret_value
        elif value + array[i] == target:
            ret_value += 1
        else:
            ret_value += backtracking(array,target,i+1,value+array[i])
    return ret_value

if __name__ == "__main__":
    n,s = map(int,input().split())
    main()