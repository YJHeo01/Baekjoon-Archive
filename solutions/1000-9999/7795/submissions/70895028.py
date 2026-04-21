t = int(input())


def binary_search(A_list,B_list):
    ret_value = 0
    left,right = 0,m-1
    correct_idx = -1
    for a in A_list:
        while left <= right:
            mid = (left + right) // 2
            if a <= B_list[mid]:
                right = mid - 1
            else:
                correct_idx = mid
                left = mid + 1
        left = (correct_idx+1)
        right = m-1
        ret_value += (correct_idx+1)
    return ret_value

        
for _ in range(t):
    n,m = map(int,input().split())
    A_list = list(map(int,input().split()))
    B_list = list(map(int,input().split()))
    A_list.sort()
    B_list.sort()
    answer = binary_search(A_list,B_list)
    print(answer)