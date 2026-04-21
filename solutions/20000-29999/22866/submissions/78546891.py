def main():
    n = int(input())
    array = [0] + list(map(int,input().split()))
    nearest_building_idx = [0] * (n+1)
    left_building_cnt = get_left_building_cnt(array,nearest_building_idx,n)
    right_building_cnt = get_right_building_cnt(array,nearest_building_idx,n)
    for i in range(1,n+1):
        if nearest_building_idx[i] == 0: print(0)
        else:print(left_building_cnt[i]+right_building_cnt[i],nearest_building_idx[i])

def get_left_building_cnt(array,nearest_building_idx,n):
    left_building_cnt = [0] * (n+1)
    stack = []
    for right_idx in range(1,n+1):
        while True:
            if stack == []: break
            left_idx = stack.pop()
            if array[left_idx] > array[right_idx]:
                nearest_building_idx[right_idx] = left_idx
                left_building_cnt[right_idx] = left_building_cnt[left_idx] + 1
                stack.append(left_idx)
                break
        stack.append(right_idx)
    return left_building_cnt

def get_right_building_cnt(array,nearest_building_idx,n):
    right_building_cnt = [0] * (n+1)
    stack = []
    for left_idx in range(n,0,-1):
        while True:
            if stack == []: break
            right_idx = stack.pop()
            if array[left_idx] >= array[right_idx]: continue
            if nearest_building_idx[left_idx] == 0 or left_idx - nearest_building_idx[left_idx] > right_idx - left_idx:
                nearest_building_idx[left_idx] = right_idx
            right_building_cnt[left_idx] = right_building_cnt[right_idx] + 1
            stack.append(right_idx)
            break
        stack.append(left_idx)
    return right_building_cnt

if __name__ == "__main__":
    main()