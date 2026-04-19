def main():
    s = list(input())
    answer = get_answer(s,0)
    print(answer)

def get_answer(s,idx):
    length = len(s)
    if length == idx: return 1
    if s[idx] == '0' or length < idx+1: return 0
    ret_value = get_answer(s,idx+1)
    if idx + 1 != length:
        if s[idx] == '1' or (s[idx] == '2' and int(s[idx+1])<7):
            ret_value += get_answer(s,idx+2)
    return ret_value % 1000000

if __name__ == "__main__":
    main()