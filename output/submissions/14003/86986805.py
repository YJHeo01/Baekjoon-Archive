def main():
    solution(list(map(int,input().split())))

def solution(array):
    length = 0
    INF = int(1e10)
    LCS = [INF] * n
    last_value = [-1] * n
    min_value_idx_of_length = []
    for i in range(n):
        value = array[i]
        target = length
        left,right = 0,length
        while left <= right:
            mid = (left+right) // 2
            if LCS[mid] >= value:
                right = mid - 1
                target = mid
            else:
                left = mid + 1
        LCS[target] = value
        if target == length:
            min_value_idx_of_length.append(i)
            length += 1
        if target != 0:
            last_value[i] = min_value_idx_of_length[target-1]
    print(length)
    get_LCS(array,last_value,min_value_idx_of_length[length-1])
    return length

def get_LCS(array,last_value,vx):
    idx_list = [vx]
    while True:
        nx = last_value[vx]
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