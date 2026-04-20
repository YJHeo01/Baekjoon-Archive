from itertools import combinations

n, m = map(int,input().split())

city = []

chicken = []
house_list = []
for i in range(n):
    city_row = list(map(int,input().split()))
    for j in range(n):
        if city_row[j] == 2:
            chicken.append((i,j))
        elif city_row[j] == 1:
            house_list.append((i,j))
    city.append(city_row)

test_case_list = list(combinations(chicken,m))
INF = int(1e9)
answer = INF

def distance_sum(test_case):
    ret_value = 0
    for house_x, house_y in house_list:
        tmp = INF
        for chicken_x, chicken_y in test_case:
            tmp = min(tmp,abs(house_x-chicken_x)+abs(house_y-chicken_y))
        ret_value += tmp
    return ret_value

for test_case in test_case_list:
    answer = min(answer,distance_sum(test_case))

print(answer)
