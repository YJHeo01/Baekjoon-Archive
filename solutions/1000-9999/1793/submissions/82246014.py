dp_a, dp_b, dp_c = [0] * 251, [0] * 251, [0] * 251

dp_a[1], dp_b[2], dp_a[2], dp_c[2] = 1,1,1,1

for i in range(3,251):
    dp_a[i] = dp_a[i-1] + dp_b[i-1] + dp_c[i-1]
    dp_b[i] = dp_a[i-2] + dp_b[i-2] + dp_c[i-2]
    dp_c[i] = dp_a[i-2] + dp_b[i-2] + dp_c[i-2]

while True:
    try:
        n = int(input())
        print(dp_a[n]+dp_b[n]+dp_c[n])
    except EOFError:
        break