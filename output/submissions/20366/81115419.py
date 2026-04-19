def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    answer = 2 *int(1e9) + 1
    for A_right in range(3,n):
        for A_left in range(A_right-2):
            A = array[A_left] + array[A_right]
            left, right = A_left + 1, A_right - 1
            while left < right:
                B = array[left]+array[right]
                cur_value = abs(A-B)
                answer = min(answer,cur_value)
                change_left = abs(A-(B - array[left] + array[left+1]))
                change_right = abs(A-(B - array[right] + array[right-1]))
                if change_left > cur_value and change_right > cur_value:
                    break
                if change_left < change_right:
                    left += 1
                else:
                    right -= 1         
    print(answer)

if __name__ == "__main__":
    main()