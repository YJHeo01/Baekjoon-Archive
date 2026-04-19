k,n = map(int,input().split())

tmp = [input() for _ in range(k)]

array = []

def sort_A(array):
    for i in range(k-1,-1,-1):
        for j in range(i):
            change = False
            left_length, right_length = len(array[j]), len(array[j+1])
            if left_length < right_length: change = True
            left_idx, right_idx = 0,0
            left_value, right_value = 0,0
            while True:
                if left_idx == left_length and right_idx == right_length or left_length != right_length:
                    break
                left_value = int(array[j][left_idx])
                left_idx += 1
                right_value = int(array[j+1][right_idx])
                right_idx += 1
                if left_value != right_value:
                    if left_value < right_value:
                        change = True
                    break
            if change:
                array[j], array[j+1] = array[j+1], array[j]

def sort_func(array):
    for i in range(n-1,-1,-1):
        for j in range(i):
            change = False
            left_length, right_length = len(array[j]), len(array[j+1])
            left_idx, right_idx = 0,0
            left_value, right_value = 0,0
            while True:
                if left_idx >= left_length and right_idx >= right_length and left_idx % left_length == 0 and right_idx %right_length == 0:
                    if len(array[j]) < len(array[j+1]): change = True
                    break
                left_value = int(array[j][left_idx%left_length])
                left_idx += 1
                right_value = int(array[j+1][right_idx%right_length])
                right_idx += 1
                if left_value != right_value:
                    if left_value < right_value:
                        change = True
                    break
            if change:
                array[j], array[j+1] = array[j+1], array[j]

sort_A(tmp)

array = []

for _ in range(n-k):
    array.append(tmp[0])

for i in tmp: array.append(i)

sort_func(array)

if array[0][0] == '0':
    print(0)
    exit(0)

for i in array: print(i,end="")