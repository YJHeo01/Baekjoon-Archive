n = int(input())

if -32768 <= n and n <= 32767:
    print("short")
elif -2147483648 <= n and n <= 2 ** 31 - 1:
    print("int")
else:
    print("long long")