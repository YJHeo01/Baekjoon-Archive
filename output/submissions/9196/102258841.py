while True:
    h,w = map(int,input().split())
    if h == 0: break
    answer = (151,151)
    for x in range(1,151):
        for y in range(x+1,151):
            if (x**2+y**2) > (h**2) + (w**2):
                if answer[0] ** 2 + answer[1] ** 2 > (x**2) + (y**2):
                    answer = (x,y)
                elif answer[0] ** 2 + answer[1] ** 2 == (x**2) + (y**2):
                    if answer[0] > x : answer = (x,y)
                else:
                    if answer[0] == 151 and x > h:
                        answer = (x,y)
                break
            if x ** 2 + y ** 2 == (h**2) + w ** 2:
                if x <= h: continue
                if answer[0] ** 2 + answer[1] ** 2 > h ** 2 + w ** 2:
                    answer = (x,y)
                else:
                    if x < answer[0]: answer = (x,y)
    print(*answer)