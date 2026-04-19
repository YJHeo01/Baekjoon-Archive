while True:
    tmp = input()
    if tmp == "END": break
    for i in reversed(tmp):
        print(i,end="")
    print()