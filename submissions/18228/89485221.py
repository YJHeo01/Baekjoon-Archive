n = int(input())

array = list(map(int,input().split()))

penguin = array.index(-1)

print(min(array[:penguin])+min(array[penguin+1:]))