def main():
    n = int(input())
    key = [0] * 8
    for i in range(8):
        key[i] = i
    command = list(map(int,input().split()))
    for c in command:
        i = -1
        for j in range(8):
            if 2 ** j  & c!= 0:
                c -= 2 ** j
                if i == -1: i = j
                else:
                    if c == 0:
                        key[i], key[j] = key[j], key[i]
                    break
    k = int(input())
    print(key[k])

if __name__  == "__main__":
    main()