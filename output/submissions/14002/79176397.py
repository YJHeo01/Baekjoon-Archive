def main():
    n = int(input())
    dp = [1] * n; last_idx = [0] * n
    for i in range(n): last_idx[i] = i
    array = list(map(int,input().split()))
    longest_length = 1
    target_idx = 0
    for i in range(n):
        for j in range(i):
            if array[j] >= array[i] or dp[i] >= dp[j] + 1:continue
            dp[i] = dp[j] + 1
            if dp[i] > longest_length:
                longest_length = dp[i]
                target_idx = i
                last_idx[i] = j
    print(longest_length)
    LIS = get_LIS(array,last_idx,target_idx)
    for i in LIS:
        print(i,end=" ")

def get_LIS(array,last_idx,vx):
    ret_value = [array[vx]]
    while True:
        nx = last_idx[vx]
        if nx == vx: break
        ret_value.append(array[nx])
        vx = nx
    ret_value.reverse()
    return ret_value

if __name__ == "__main__":
    main()