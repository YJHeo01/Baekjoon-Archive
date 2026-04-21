def main():
    n = int(input())
    array = [['.']*20 for _ in range(10)]
    for _ in range(n):
        tmp = input()
        array[ord(tmp[0])-ord('A')][int(tmp[1:])-1] = 'o'
    for i in range(10):
        for j in range(20):
            print(array[i][j],end="")
        print()
    
if __name__ == "__main__":
    main()