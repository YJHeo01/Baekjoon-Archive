king, stone, n = input().split()

n = int(n)
king, stone = list(king), list(stone)

king_x, king_y = int(king[1]) - 1, ord(king[0]) - ord('A')

stone_x, stone_y = int(stone[1]) - 1, ord(stone[0]) - ord('A')

command = []

for _ in range(n):
    tmp = input()
    command.append(tmp)

for c in command:
    king_tmp_x, king_tmp_y = king_x,king_y
    stone_tmp_x, stone_tmp_y = stone_x,stone_y
    if c == 'R':
        king_tmp_y += 1
    elif c == 'L':
        king_tmp_y -= 1
    elif c == 'B':
        king_tmp_x -= 1
    elif c == 'T':
        king_tmp_x += 1
    elif c == 'RT':
        king_tmp_y += 1
        king_tmp_x += 1
    elif c == 'LT':
        king_tmp_y -= 1
        king_tmp_x += 1
    elif c == 'RB':
        king_tmp_y += 1
        king_tmp_x -= 1
    else:
        king_tmp_y -= 1
        king_tmp_x -= 1
    if stone_tmp_x == king_tmp_x and stone_tmp_y ==  king_tmp_y:
        stone_tmp_x = stone_x + (king_tmp_x - king_x)
        stone_tmp_y = stone_y + (king_tmp_y - king_y)
    if stone_tmp_x < 0 or stone_tmp_y < 0 or king_tmp_x < 0 or king_tmp_y < 0 or stone_tmp_x >= 8 or stone_tmp_y >= 8 or king_tmp_x >= 8 or king_tmp_y >= 8:
        continue
    else:
        stone_x, stone_y = stone_tmp_x, stone_tmp_y
        king_x, king_y = king_tmp_x, king_tmp_y
print(chr(king_y+ord('A'))+str(king_x+1))
print(chr(stone_y+ord('A'))+str(stone_x+1))