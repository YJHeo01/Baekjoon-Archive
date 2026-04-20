def main():
    t = int(input())
    for _ in range(t):
        s = list(input())
        print(answer(s))

def answer(s):
    length = len(s); idx = 0; last_pattern = 0
    if length == 1: return 'NO'
    last_pattern = 1
    if s[0] == '0':
        if s[1] == '0': return 'NO'
        idx = 2; last_pattern = 2
    while True:
        if idx == length: return 'YES'
        if idx == -1: return 'NO'
        if s[idx] == '0':
            if idx + 1 == length: return 'NO'
            idx = second_pattern(idx)
            if s[idx-1] == '0':
                if last_pattern != 1: return 'NO'
                idx -= 2
                if s[idx-1] == '0': return 'NO'
            last_pattern = 2
        if idx + 2 >= length: return 'NO'
        idx = first_pattern(s,idx)

def first_pattern(s,idx):
    if s[idx+1] == '1' or s[idx+2] == '1': return -1
    idx += 3; length = len(s)
    while True:
        if idx == length: return -1
        if s[idx] == '1': break
        idx += 1
    while True:
        if idx == length or s[idx] == '0':break
        idx += 1
    return idx

def second_pattern(idx):
    return idx + 2

if __name__ == "__main__":
    main()