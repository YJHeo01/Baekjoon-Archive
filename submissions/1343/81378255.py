def main():
    array = list(input())
    length = len(array)
    left = 0
    while True:
        if left >= length:
            break
        if array[left] == 'X':
            right = left
            while True:
                right += 1
                if right == length or array[right] =='.':
                    break
            if (right-left) % 2 == 1:
                print(-1)
                return
            elif (right-left) % 4 == 0:
                for i in range(left,right):
                    array[i] = 'A'
            else:
                for i in range(left,right-2):
                    array[i] = 'A'
                for i in range(right-2,right):
                    array[i] = 'B'
            left = right
        left += 1
    for i in array:
        print(i,end="")
if __name__ == "__main__":
    main()