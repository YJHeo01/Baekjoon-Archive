from bisect import bisect_right
import sys

input = sys.stdin.readline

x = 0
def main():
    global x
    n = int(input())
    trash = []
    cnt = 0
    answer = 0
    for _ in range(n):
        tmp = list(map(int,input().split()))
        if tmp[0] == 1:
            trash.append(tmp[1])
            cnt += 1
        else:
            if cnt == 0: continue
            trash.sort()
            right = bisect_right(trash,x)
            left = right - 1
            while True:
                if left < 0 or right >= cnt: break
                if x - trash[left] <= trash[right] - x:
                    answer += (x-trash[left])
                    x = trash[left]
                    left -= 1
                else:
                    answer += (trash[right] - x)
                    x = trash[right]
                    right += 1
            if left < 0:
                answer += (trash[cnt-1]-x)
                x = trash[cnt-1]
            else:
                answer += (x-trash[0])
                x = trash[0]
            trash = []
            cnt = 0
    print(answer)
        

if __name__ == "__main__":
    main()