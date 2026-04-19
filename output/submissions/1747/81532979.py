def main():
    n = int(input())
    if n <= 2: print(2)
    INF = 10000000
    prime = [True] * (INF)
    prime[0], prime[1] = False, False
    for i in range(3,INF,2):
        if prime[i] == True:
            for j in range(i+i,INF,i):
                prime[j] = False
            if i < n: continue
            correct_target = True
            tmp = str(i)
            length = len(tmp)
            for j in range(length//2):
                if tmp[j] != tmp[length-1-j]:
                    correct_target = False
                    break
            if correct_target == True:
                print(i)
                return

if __name__ == "__main__":
    main()