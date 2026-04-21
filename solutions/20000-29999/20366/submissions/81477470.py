import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    answer = int(1e9) * 2 + 1
    for A_right in range(3,n):
        for A_left in range(A_right-2):
            A_value = array[A_left] + array[A_right]
            B_left, B_right = A_left + 1, A_right - 1
            while B_left < B_right:
                B_value = array[B_left] + array[B_right]
                answer = min(answer,abs(B_value-A_value))
                if B_value > A_value:
                    B_right -= 1
                elif B_value < A_value:
                    B_left += 1
                else:
                    break
    print(answer)

if __name__ == "__main__":
    main()