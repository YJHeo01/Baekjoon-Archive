def shot(keyboard,c):
    for x in range(4):
        for y in range(10):
            if keyboard[x][y] == c:
                return x,y

keyboard = [list(input()) for _ in range(4)]
shotgun = list(input())
target_x, target_y = 0,0
for c in shotgun:
    tmp_x, tmp_y = shot(keyboard,c)
    target_x += tmp_x; target_y += tmp_y

target_x = target_x // 9; target_y = target_y // 9

print(keyboard[target_x][target_y])