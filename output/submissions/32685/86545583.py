password = 0
for i in range(3):
    num = int(input())
    password <<= 4
    tmp = 0
    for j in range(4):
        if num & 1:
            tmp += 2 ** j
        num >>= 1
    password += tmp
password = str(password)
while True:
    if len(password) >= 4: break
    password = '0' + password
print(password)