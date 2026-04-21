n,x = map(int,input().split())

member_list = list(map(int,input().split()))

member_sum = sum(member_list)

if member_sum % x == 0:
    print(1)
else:
    print(0)