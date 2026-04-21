import sys, heapq

input = sys.stdin.readline

x,y,m = map(int,input().split())

fight = []

for i in range(x):
    heapq.heappush(fight,(int(input()),-i-1))

heal = []

for i in range(y):
    heapq.heappush(heal,(int(input()),i+1))

answer = []

while fight:
    fight_value, fight_idx = heapq.heappop(fight)
    
    while heal:
        if m > fight_value: break
        heal_value, heal_idx = heapq.heappop(heal)
        answer.append(heal_idx)
        m += heal_value
    m -= fight_value
    if m <= 0:
        print(0)
        exit(0)
    answer.append(fight_idx)

while heal:
    heal_value, heal_idx = heapq.heappop(heal)
    answer.append(heal_idx)

for i in answer: print(i)
