import heapq

minus_value_list = []
plus_value_list = []


def heappush(value):
    global minus_value_list,plus_value_list
    if value > 0:
        heapq.heappush(plus_value_list,-value)
    else:
        heapq.heappush(minus_value_list,value)

def sum_value(num_list,plus_minus):
    return_value = 0
    while len(num_list)>=2:
        value1 = (-plus_minus)*heapq.heappop(num_list)
        value2 = (-plus_minus)*heapq.heappop(num_list)
        return_value += max((value1*value2),(value1+value2))
    if num_list != []:
        return (return_value,num_list[0])
    else:
        return (return_value,0)

def sum_minus_value(num_list):
    value1, value2 = sum_value(num_list,-1)
    return (value1+value2)

def sum_plus_value(num_list):
    value1, value2 = sum_value(num_list,1)
    return (value1-value2)

def find_answer():
    value1 = sum_minus_value(minus_value_list)
    value2 = sum_plus_value(plus_value_list)
    return (value1+value2)

n = int(input())

for _ in range(n):
    value = int(input())
    heappush(value)

answer = find_answer()

print(answer)