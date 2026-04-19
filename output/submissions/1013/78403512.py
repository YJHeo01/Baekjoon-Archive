def main():
    t = int(input())
    for _ in range(t):
        print(answer())

def answer():
    s = list(input())
    length = len(s); idx = 0
    while True:
        if idx == length: return 'YES'
        if s[idx] == '0':
            if idx + 1 == length or s[idx+1] == '0': return 'NO'
            idx += 2
        else:
            if idx + 2 >= length or s[idx+1] == '1' or s[idx+2] == '1':
                return 'NO'
            idx += 3
            while True:
                if idx == length: return 'NO'
                if s[idx] == '1': break
                idx += 1
            while True:
                if idx == length or s[idx] == '0':break
                idx += 1

if __name__ == "__main__":
    main()