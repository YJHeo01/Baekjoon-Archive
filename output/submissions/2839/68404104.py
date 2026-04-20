n = int(input())

five = n // 5

while True:
    tmp = n - five * 5
    if tmp % 3==0:
        three = tmp // 3
        break
    elif five <= 0:
        three = -1
        break
    five -= 1

print(five+three)