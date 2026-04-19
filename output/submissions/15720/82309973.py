b,c,d = map(int,input().split())
burger = sorted(list(map(int,input().split())))
side = sorted(list(map(int,input().split())))
juice = sorted(list(map(int,input().split())))

answer = sum(burger)+sum(side)+sum(juice)
print(answer)
for _ in range(min(b,c,d)):
    answer -= (burger.pop()) // 10
    answer -= (side.pop()) // 10
    answer -= (juice.pop()) // 10

print(answer)
