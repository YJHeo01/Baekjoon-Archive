def main():
    n,m = map(int,input().split())
    array = get_array(n)
    answer = get_answer(array,n,m)
    print(answer)

def get_array(n):
    array = []
    for _ in range(n): array.append(list(input()))
    return array

def get_answer(array,n,m):
    ret_value_A, ret_value_B = 0,0
    for i in range(n):
        for j in range(m):
            ret_value_A += int(array[i][j]) * 10 ** (m-j-1)
            ret_value_B += int(array[i][j]) * 10 ** (n-i-1)
    return max(ret_value_A,ret_value_B)

if __name__ == "__main__":
    main()