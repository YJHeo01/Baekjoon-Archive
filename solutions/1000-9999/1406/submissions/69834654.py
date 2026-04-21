import sys
input = sys.stdin.readline

string = list(input().rstrip())

l = len(string)

cursor = l

m = int(input().rstrip())

for _ in range(m):
    tmp = list(input().split())
    if tmp[0] == 'P':
        string = string[:cursor]+[tmp[1]]+string[cursor:]
        l += 1
        cursor += 1
    elif tmp[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1
    elif tmp[0] == 'D':
        if cursor == l:
            continue
        cursor += 1
    else:
        if cursor == 0:
            continue
        string = string[:cursor-1]+string[cursor:]
        cursor -= 1
        l-=1
for i in string:
    print(i,end="")