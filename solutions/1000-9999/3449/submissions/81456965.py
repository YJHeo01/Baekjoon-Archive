def main():
    n = int(input())
    for _ in range(n):
        a = list(input())
        b = list(input())
        length = len(a)
        answer = 0
        for i in range(length):
            if a[i] != b[i]:
                answer += 1
        print("Hamming distance is " + str(answer)+".")

if __name__ == "__main__":
    main()