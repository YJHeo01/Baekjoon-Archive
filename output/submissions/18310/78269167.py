import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    house = list(map(int,input().split()))
    house.sort()
    house_cnt = get_house_idx(house)
    last_idx = house[0]
    answer_idx = last_idx
    min_distance = get_first_house_distance(house)
    tmp_distance = min_distance
    left, right = 0, n - house_cnt[last_idx]
    for cur_idx in range(house[0]+1,100001):
        if house_cnt[cur_idx] == 0: continue
        left += house_cnt[last_idx]
        tmp_distance -= right * (cur_idx-last_idx)
        right -= house_cnt[cur_idx]
        tmp_distance += left * (cur_idx-last_idx)
        last_idx = cur_idx
        if min_distance > tmp_distance:
            min_distance = tmp_distance
            answer_idx = cur_idx
    print(answer_idx)


def get_house_idx(house):
    house_idx = [0] * 100001
    for x in house:
        house_idx[x] += 1
    return house_idx
    
def get_first_house_distance(house):
    ret_value = 0
    for x in house:
        ret_value += (x-house[0])
    return ret_value

if __name__ == "__main__":
    main()