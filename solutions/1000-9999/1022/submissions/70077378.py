r1, c1, r2, c2 = map(int,input().split())

mid = max(abs(r1),abs(c1),abs(r2),abs(c2))

dx = [0,-1,0,1]
dy = [1,0,-1,0]

length = mid * 2 + 1
paper = [[0]*length for _ in range(length)]





def answer():
    global paper
    x,y = mid,mid
    paper[x][y] = 1
    value = 2
    move_distance = 1
    while 1:
        for i in range(4):
            for _ in range(move_distance):
                if value > length ** 2:
                    return                
                x += dx[i]
                y += dy[i]
                paper[x][y] = value
                value += 1
            if i % 2 == 1:
                move_distance += 1
                if move_distance == length:
                    move_distance -= 1

answer()
max_digit = 0
digit_list = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
for i in range(mid+r1,mid+r2+1):
    for j in range(mid+c1,mid+c2+1):
        tmp = paper[i][j]
        k = 1
        while 10 ** k <= tmp:
            k+=1
        digit_list[i-mid-r1][j-mid-c1] = k
        max_digit = max(max_digit,k)
        
        

for i in range(mid+r1,mid+r2+1):
    for j in range(mid+c1,mid+c2+1):
        for _ in range(max_digit-digit_list[i-mid-r1][j-mid-c1]):
            print(" ",end="") 
        print(paper[i][j],end=" ")
    print()