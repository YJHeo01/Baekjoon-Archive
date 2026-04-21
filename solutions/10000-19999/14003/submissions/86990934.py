def main():
    solution(list(map(int,input().split())))

def solution(array):
    length = 0
    INF = int(1e10)
    LCS = [INF] * n
    last_idx = [-1] * n
    min_val_idx = []
    for i in range(n):
        value = array[i]
        target = length
        left,right = 0,length-1
        while left <= right:
            mid = (left+right) // 2
            if LCS[mid] >= value:
                right = mid - 1
                target = mid
            else:
                left = mid + 1
        LCS[target] = value
        if target == length:
            min_val_idx.append(i)
            length += 1
        else:
            min_val_idx[target] = i
        if target != 0:
            last_idx[i] = min_val_idx[target-1]
    print(length)
    print_LCS(array,last_idx,min_val_idx[length-1])

def print_LCS(array,last_idx,vx):
    idx_list = [vx]
    while True:
        nx = last_idx[vx]
        if nx == -1: break
        idx_list.append(nx)
        vx = nx
    idx_list.reverse()
    for i in idx_list:
        print(array[i],end=" ")
    return idx_list

if __name__ == "__main__":
    n = int(input())
    main()