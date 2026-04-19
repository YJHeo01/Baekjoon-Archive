input()
a = 0
for _ in range(2):
    for i in map(int,input().split()):a+=abs(i)
print(a)