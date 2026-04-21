sab = int(input())
fm = sum(map(int,input().split()))

if sab <= 240 or fm >= sab:
    print("high speed rail")
else:
    print("flight")