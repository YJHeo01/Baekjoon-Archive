n,m,l,k = map(int,input().split())

star = []

for _ in range(k):
    star.append(list(map(int,input().split())))

dx = [0,l,0,l]
dy = [0,0,l,l]
direction_type_dx = [1,1,-1,-1]
direction_type_dy = [1,-1,1,-1]

answer = k
for x,y in star:
    for i in range(4):
        for j in range(4):
            tmp = 0
            x1 = x
            y1 = y
            x2 = x + dx[i] * direction_type_dx[j]
            y2 = y + dy[i] * direction_type_dy[j]
            if x1 > x2:
                x1,x2 = x2,x1
            if y1 > y2:
                y1,y2 = y2,y1
            for star_x, star_y in star:
                if star_x < x1 or star_y < y1 or star_x > x2 or star_y > y2:
                    tmp += 1
            answer = min(answer,tmp)

print(answer)