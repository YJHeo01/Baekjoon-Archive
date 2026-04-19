import sys

input = sys.stdin.readline

def main():
    while True:
        name, age, kg = input().rstrip().split()
        if name == '#' and age == '0' and kg == '0': break
        print(name,end=" ")
        if int(age) > 17 or int(kg) >= 80:
            print('Senior')
        else:
            print('Junior')

if __name__ == "__main__":
    main()