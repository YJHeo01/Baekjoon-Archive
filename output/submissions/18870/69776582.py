n = int(input())

Xn = list(map(int,input().split()))

num_list = []

l = -1
for x in Xn:
    if x not in num_list:
        num_list.append(x)
        l += 1

num_list.sort()

for i in range(n):
    left = 0
    right = l
    while left <= right:
        mid = (left+right) // 2
        if num_list[mid] < Xn[i]:
            left = mid + 1
        elif num_list[mid] > Xn[i]:
            right = mid - 1
        else:
            Xn[i] = mid
            break

for x in Xn:
    print(x,end = " ")