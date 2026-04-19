def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 2 *int(1e9) + 1
    for A_right in range(3,n):
        for A_left in range(A_right-2):
            A = array[A_left] + array[A_right]
            for B_right in range(A_left+2,A_right):
                for B_left in range(A_left,B_right):
                    answer = min(answer,abs(A-(array[B_left]+array[B_right])))
    print(answer)

if __name__ == "__main__":
    main()