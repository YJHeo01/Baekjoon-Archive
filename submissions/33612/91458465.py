n = int(input())

year = 2024
month = 8

while True:
    n -= 1
    if n == 0: break
    month += 7
    if month > 12:
        year += 1
        month -= 12

print(year,month)