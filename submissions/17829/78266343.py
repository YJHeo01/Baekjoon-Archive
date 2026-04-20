import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    array = get_array(n)
    answer = solution(array,(0,n),(0,n))
    print(answer)

def get_array(n):
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    return array

def solution(array,A,B):
    x1,x2 = A; y1,y2 = B
    if x2 - x1 == 2: return(second_value(array[x1][y1],array[x1+1][y1],array[x1][y1+1],array[x1+1][y1+1]))
    mid_x, mid_y = (x1+x2) // 2, (y1+y2) // 2
    value_A = solution(array,(x1,mid_x),(y1,mid_y))
    value_B = solution(array,(x1,mid_x),(mid_y,y2))
    value_C = solution(array,(mid_x,x2),(y1,mid_y))
    value_D = solution(array,(mid_x,x2),(mid_y,y2))
    return second_value(value_A,value_B,value_C,value_D)

def second_value(value_A,value_B,value_C,value_D):
    num_list = [value_A,value_B,value_C,value_D]
    num_list.sort()
    return num_list[2]

if __name__ == "__main__":
    main()