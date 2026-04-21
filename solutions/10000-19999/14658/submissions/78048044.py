import sys

input = sys.stdin.readline

def main():
    star_list = get_star_list()
    answer = 0
    for star in star_list:
        answer = max(answer,left(star_list,star),right(star_list,star),high(star_list,star),low(star_list,star))
    print(k-answer)

def get_star_list():
    star = []
    for _ in range(k):
        star.append(list(map(int,input().split())))
    return star

def left(star_list,star):
    ret_value = 0
    x,y = star
    y1,y2 = y,y+l
    for i in range(l):
        x1, x2 = x - i, x - i + l
        tmp = 0
        for star_x, star_y in star_list:
            if star_x < x1 or star_x > x2 or star_y < y1 or star_y > y2:
                continue
            tmp += 1
        ret_value = max(ret_value,tmp)
    return ret_value

def right(star_list,star):
    ret_value = 0
    x,y = star
    y1,y2 = y-l,y
    for i in range(l):
        x1, x2 = x - i, x - i + l
        tmp = 0
        for star_x, star_y in star_list:
            if star_x < x1 or star_x > x2 or star_y < y1 or star_y > y2:
                continue
            tmp += 1
        ret_value = max(ret_value,tmp)
    return ret_value

def high(star_list,star):
    ret_value = 0
    x,y = star
    x1,x2 = x,x+l
    for i in range(l):
        y1, y2 = y - i, y - i + l
        tmp = 0
        for star_x, star_y in star_list:
            if star_x < x1 or star_x > x2 or star_y < y1 or star_y > y2:
                continue
            tmp += 1
        ret_value = max(ret_value,tmp)
    return ret_value

def low(star_list,star):
    ret_value = 0
    x,y = star
    x1,x2 = x-l,x
    for i in range(l):
        y1, y2 = y - i, y - i + l
        tmp = 0
        for star_x, star_y in star_list:
            if star_x < x1 or star_x > x2 or star_y < y1 or star_y > y2:
                continue
            tmp += 1
        ret_value = max(ret_value,tmp)
    return ret_value

if __name__ == "__main__":
    n,m,l,k = map(int,input().split())
    if n <= l and m <= l:
        print(0)
        exit(0)
    main()