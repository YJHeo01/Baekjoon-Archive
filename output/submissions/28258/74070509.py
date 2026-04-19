r1,c1 = -1,-1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
check = [[False]*10 for _ in range(10)]
for x in range(0,10):
    for y in range(x%2,10,2):
        print("? " + str(x) + " "+ str(y))
        check[x][y] = True
        n = int(input())
        if n == 1:
            r1,c1 = x,y
            break
        for k in range(4):
            check_x = x + dx[k]
            check_y = y + dy[k]
            if check_x < 0 or check_y < 0 or check_x > 9 or check_y > 9:
                continue
            check[check_x][check_y] = True
    if r1 != -1:
        break
if r1 == 9 and c1 == 8:
    r2, c2 = 9,9
else:
    for i in range(4):
        r2 = r1 + dx[i]
        c2 = c1 + dy[i]
        if r2 < 0 or c2 < 0 or r2 > 9 or c2 > 9 or check[r2][c2] == True:
            continue
        print("? " + str(r2) + " "+ str(c2))
        n = int(input())
        if n == 1:
            break

print("! " + str(r1) + " " + str(c1) + " " + str(r2) + " " + str(c2))