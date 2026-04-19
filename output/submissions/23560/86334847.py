def main():
    n = int(input())
    array = []
    for _ in range(n):
        array += [0,1,0]
    answer = backtracking(array,0,3*n-1,0)
    print(answer)

def backtracking(array,left,right,idx):
    if left + 1 == right: return 1
    ret_value = 0
    if array[left] == idx % 2: ret_value += backtracking(array,left+1,right,(idx+1)%3)
    if array[right] == idx % 2: ret_value += backtracking(array,left,right-1,(idx+1)%3)
    return ret_value

if __name__ == "__main__":
    main()