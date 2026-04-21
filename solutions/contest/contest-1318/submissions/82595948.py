n = int(input())
array = input()
if n == 1:
    print(array)
    exit(0)
print(array[:2],end="")
idx = 2
while True:
    if idx >= n:
        break
    if array[idx-2:idx] == "PS" and (array[idx]=='4' or array[idx] == '5'):
        array = array[:idx] + array[idx+1:]
        n -= 1
    else:
        print(array[idx],end="")
        idx += 1