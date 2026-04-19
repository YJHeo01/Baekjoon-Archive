def main():
    answer = 0
    x = int(input())
    for i in range(7):
        if x & (2**i) != 0: answer += 1
    print(answer)
        
if __name__ == "__main__":
    main()