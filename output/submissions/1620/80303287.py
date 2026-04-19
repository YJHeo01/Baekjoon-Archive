import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    numConvertStr = ['']
    strConvertNum = {}
    for i in range(1,n+1):
        name = input().rstrip()
        numConvertStr.append(name)
        strConvertNum[name] = i
    for _ in range(m):
        value = input().rstrip()
        try:
            answer = numConvertStr[int(value)]
        except ValueError:
            answer = strConvertNum[value]
        print(answer)

if __name__ == "__main__":
    main()