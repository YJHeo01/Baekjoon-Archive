array = list(input())
for i in range(10):
    if array[i] == '@':
        robot = i
    elif array[i] == '#':
        box = i
    elif array[i] == '!':
        target = i
    else:
        continue
if robot < box and box < target:
    print(target-robot-1)
elif target < box and box < robot:
    print(robot-target-1)
else:
    print(-1)