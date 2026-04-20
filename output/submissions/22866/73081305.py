n = int(input())

building_list = [0] + list(map(int,input().split()))

def search_left_building(idx):
    building_cnt = 0
    near_idx = n+2
    last_max = building_list[idx]
    for i in range(idx-1,0,-1):
        if building_list[i] > last_max:
            if building_cnt == 0:
                near_idx = i
            building_cnt += 1
            last_max = building_list[i]
    return building_cnt,near_idx

def search_right_building(idx):
    building_cnt = 0
    near_idx = n+2
    last_max = building_list[idx]
    for i in range(idx+1,n+1):
        if building_list[i] > last_max:
            if building_cnt == 0:
                near_idx = i
            building_cnt += 1
            last_max = building_list[i]
    return building_cnt,near_idx

for i in range(1,n+1):
    building_cnt_L, near_idx_L = search_left_building(i)
    building_cnt_R, near_idx_R = search_right_building(i)
    building_cnt = building_cnt_L + building_cnt_R
    if building_cnt == 0:
        print(0)
    else:
        print(building_cnt,end=" ")
        if abs(near_idx_L-i) <= abs(near_idx_R-i):
            print(near_idx_L)
        else:
            print(near_idx_R)