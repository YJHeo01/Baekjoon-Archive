import sys

input = sys.stdin.readline

def main():
    star_list = get_star_list()
    answer = k - solution(star_list)
    print(answer)

def get_star_list():
    star_list = []
    for _ in range(k):
        star_list.append(list(map(int,input().split())))
    return star_list

def solution(star_list):
    ret_value = 0
    dx = [-1,0]
    dy = [0,-1]
    for star in star_list:
        x,y = star
        for i in range(length):
            for k in range(2):
                x1 = x + i * dx[k]; x2 = x1 + length
                y1 = y + i * dy[k]; y2 = y1 + length
                ret_value = max(ret_value,get_star_cnt(star_list,(x1,x2),(y1,y2)))
                x2 = x + i * dx[k]; x1 = x2 - length
                y2 = y + i * dy[k]; y1 = y2 - length
                ret_value = max(ret_value,get_star_cnt(star_list,(x1,x2),(y1,y2)))
    return ret_value

def get_star_cnt(star_list,x_range,y_range):
    x1,x2 = x_range; y1,y2 = y_range
    if x1 < 0 or y1 < 0 or x2 > n or y2 > m: return 0
    ret_value = 0
    for x,y in star_list:
        if x < x1 or x > x2 or y < y1 or y > y2: continue
        ret_value += 1
    return ret_value

if __name__ == "__main__":
    n,m,length,k = map(int,input().split())
    main()