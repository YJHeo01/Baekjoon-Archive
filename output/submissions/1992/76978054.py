n = int(input())

array = []

for _ in range(n):
    array.append(list(input()))

def solution(array,start,end):
    start_x, start_y = start
    end_x, end_y = end
    compression = True
    value = array[start_x][start_y]
    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            if array[x][y] != value:
                compression = False
                print('(',end="")
                mid_x = (start_x+end_x) // 2
                mid_y = (start_y+end_y) // 2
                solution(array,(start_x,start_y),(mid_x,mid_y))
                solution(array,(start_x,mid_y),(mid_x,end_y))
                solution(array,(mid_x,start_y),(end_x,mid_y))
                solution(array,(mid_x,mid_y),(end_x,end_y))
                print(')',end="")
                break
        if compression == False:
            break
    if compression == True:
        print(value,end="")

solution(array,(0,0),(n,n))