n,m,l,k = map(int,input().split())

stars = []
for i in range(k):
    x,y = map(int,input().split())
    stars.append((x,y))
answer = 0
for star in stars:
    tmp = 0
    for star_ in stars:
        for i in range(l):
            if star_[0] <= star[0] + i and star[0] - l + i <= star_[0] and star_[1] <= star[1] + i and star[1] - l + i <= star_[1]:
                tmp += 1
        answer = max(tmp,answer)
        tmp = 0
    for star_ in stars:
        for i in range(l):
            if star_[0] >= star[0] - i and star[0] + l - i >= star_[0] and star_[1] >= star[1] - i and star[1] + l - i >= star_[1]:
                tmp += 1
        answer = max(tmp,answer)
        tmp = 0
    for star_ in stars:
        for i in range(l):
            if star_[0] <= star[0] + i and star[0] -l + i <= star_[0] and star_[1] >= star[1] - i and star[1] + l - i >= star_[1]:
                tmp += 1
        answer = max(tmp,answer)
        tmp = 0
    for star_ in stars:
        for i in range(l):
            if star_[0] >= star[0] - i and star[0] + l - i >= star_[0] and star_[1] <= star[1] + i and star[1] - l + i<= star_[1]:
                tmp += 1
        answer = max(tmp,answer)
        tmp = 0

print(k-answer)