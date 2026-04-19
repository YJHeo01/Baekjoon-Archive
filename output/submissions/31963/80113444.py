import math

def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 0
    for i in range(1,n):
        if array[i] >= array[i-1]: continue
        tmp = math.ceil(math.log2(math.ceil(array[i-1]/array[i])))
        answer += tmp
        array[i] *= 2 ** tmp
    print(answer)

if __name__ == "__main__":
    main()