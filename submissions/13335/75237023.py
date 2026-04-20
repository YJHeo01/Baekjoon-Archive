from collections import deque

n,w,l = map(int,input().split())

bridge = deque([0]*w)
bridge_weight = 0
car = deque(list(map(int,input().split())))

time = 0

while car:
    time += 1
    escape_car = bridge.popleft()
    bridge_weight -= escape_car
    if bridge_weight + car[0] > l:
        bridge.append(0)
    else:
        new_car = car.popleft()
        bridge.append(new_car)
        bridge_weight += new_car

while bridge_weight != 0:
    time += 1
    escape_car = bridge.popleft()
    bridge_weight -= escape_car

print(time)