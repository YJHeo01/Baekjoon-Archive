import sys

input = sys.stdin.readline

def main():
    q = int(input())
    error = False
    answer = 0
    right = INF
    left = -INF
    for i in range(1,q+1):
        value, updown = input().split()
        value = int(value)
        if updown == '^': left = max(left,value)
        else: right = min(right, value)
        if left + 1 == right - 1 and answer == 0:
            answer = i
        if left > right:
            error = True
            answer = i
            break
    if answer == 0:
        print("Hmm...")
    elif error:
        print("Paradox!")
    else:
        print("I got it!")
    if answer != 0:
        print(answer)

if __name__ == "__main__":
    INF = 10 ** 18
    main()