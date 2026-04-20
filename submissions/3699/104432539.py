t = int(input())

for _ in range(t):
    h,l = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(l):
            if arr[i][j] != -1:
                answer += 20 * i
    for row in arr:
        pos = [-1] * (h*l+1)
        pos[0] = 0
        car = [0]
        for i in range(l):
            if row[i] == -1: continue
            pos[row[i]] = i
            car.append(row[i])
        car.sort()
        length = len(car)
        for right in range(1,length):
            left = right - 1
            tmp = abs(pos[car[right]]-pos[car[left]])
            answer += 5 * min(tmp,l-tmp)

    print(answer)