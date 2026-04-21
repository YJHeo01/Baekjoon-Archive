import sys

input = sys.stdin.readline

n,c = map(int,input().split())

house_list = []
for _ in range(n):
    house_list.append(int(input()))

start = 1
end = house_list[-1] - house_list[0]
answer = end

while start <= end:
    mid = (start+end) // 2
    house = house_list[0]
    cnt = 1
    for i in range(1,n):
        if house_list[i] >= house + mid:
            house = house_list[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)