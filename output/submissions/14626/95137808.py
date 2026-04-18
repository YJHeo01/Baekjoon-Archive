isbn = input()

star_idx = 0

for i in range(13):
    if isbn[i] == '*':
        star_idx = i
        break

for star_value in range(10):
    tmp = 0
    for i in range(12):
        if star_idx == i:
            num = star_value
        else:
            num = int(isbn[i])
        if i % 2 == 0:
            tmp += num
        else:
            tmp += 3 * num
    if star_idx == 12:
        m = star_value
    else:
        m = int(isbn[12])
    if m == (10 - tmp%10) % 10:
        print(star_value)
        break