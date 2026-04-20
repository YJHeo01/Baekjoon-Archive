from itertools import permutations

n,m,k = map(int,input().split())

original_array = []

for _ in range(n):
    original_array.append(list(map(int,input().split())))

data = [0] * k

for i in range(1,k):
    data[i] = i

test_case_list = list(permutations(data,k))
command = []

for _ in range(k):
    command.append(list(map(int,input().split())))

def set_tmp_array(original):
    tmp_array = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp_array[i][j] = original[i][j]
    return tmp_array

def move_high(array,row,y_range):
    for column in range(y_range[0],y_range[1],-1):
        array[row][column], array[row][column-1] = array[row][column-1],array[row][column]

def move_left(array,x_range,column):
    for row in range(x_range[0],x_range[1]):
        array[row][column], array[row+1][column] = array[row+1][column],array[row][column]
def move_low(array,row,y_range):
    for column in range(y_range[0],y_range[1]):
        array[row][column], array[row][column+1] = array[row][column+1],array[row][column]

def move_right(array,x_range,column):
    for row in range(x_range[0],x_range[1]+1,-1):
        array[row][column], array[row-1][column] = array[row-1][column],array[row][column]

def move_array(array,cal):
    r,c,s = cal
    r -= 1; c-=1
    for k in range(s,0,-1):
        move_high(array,r-k,[c+k,c-k])
        move_left(array,[r-k,r+k],c-k)
        move_low(array,r+k,[c-k,c+k])
        move_right(array,[r+k,r-k],c+k)


answer = 1000000

for test_case in test_case_list:
    tmp_array = set_tmp_array(original_array)
    for idx in test_case:
        move_array(tmp_array,command[idx])
    for row in tmp_array:
        answer = min(answer,sum(row))

print(answer)