n = int(input())
start, end = input().split('*')
start_length, end_length = len(start), len(end)
for _ in range(n):
    tmp = input()
    if len(tmp) >= (start_length + end_length) and start == tmp[:start_length] and end == tmp[len(tmp)-end_length:]:
        print("DA")
    else:
        print("NE")