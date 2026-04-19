def main():
    direction = 0
    for _ in range(10):
        command = int(input())
        if command == 1:
            direction += 1
        elif command == 2:
            direction += 2
        else:
            direction -= 1
        direction %= 4
    array = ['N','E','S','W']
    print(array[direction])

if __name__ == "__main__":
    main()