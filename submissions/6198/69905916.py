import sys

input = sys.stdin.readline

n = int(input())

building = []
top = []
answer_list = [0] * n
for _ in range(n):
    building.append(int(input()))

answer = 0

for i in range(n-1,-1,-1):
    while 1:
        if top == []:
            top.append(i)
            answer += (n-1-i)
            break
        else:
            high_building_idx = top.pop()
            if building[high_building_idx] >= building[i]:
                answer += (high_building_idx-i-1)
                top.append(high_building_idx)
                top.append(i)
                break
    
print(answer)