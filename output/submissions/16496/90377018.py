n = int(input())

array = list(input().split())

for i in range(n-1,-1,-1):
    for j in range(i):
        change = False
        left_length, right_length = len(array[j]), len(array[j+1])
        left_idx, right_idx = 0,0
        left_value, right_value = 0,0
        while True:
            finish = True
            if left_idx != left_length:
                left_value = int(array[j][left_idx])
                left_idx += 1
                finish = False
            if right_idx != right_length:
                right_value = int(array[j+1][right_idx])
                right_idx += 1
                finish = False
            if finish: 
                if len(array[j]) < len(array[j+1]):
                    change = True
                break
            if left_value != right_value:
                if left_value < right_value:
                    change = True
                break
        if change:
            array[j], array[j+1] = array[j+1], array[j]

if array[0][0] == '0':
    print(0)
    exit(0)

for i in array: print(i,end="")