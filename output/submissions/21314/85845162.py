def main():
    minkyum = input()
    length = len(minkyum)
    max_num = get_max_num(minkyum, length)
    min_num = get_min_num(minkyum, length)
    print(max_num)
    print(min_num)
    

def get_max_num(minkyum,length):
    last_k_idx, idx = -1, 0
    max_num= ""
    
    while True:
        if idx == length: break
        if minkyum[idx] == 'K':
            max_num += '5'
            for _ in range(idx-last_k_idx-1): max_num += '0'
            last_k_idx = idx
        idx += 1

    for _ in range(last_k_idx,length-1): max_num += '1'

    return max_num

def get_min_num(minkyum,length):
    last_k_idx, idx = -1, 0
    min_num = ""

    while True:
        if idx == length: break
        if minkyum[idx] == 'K':
            if last_k_idx != idx - 1: min_num += '1'
            if idx-last_k_idx-2 > 0:
                for _ in range(idx-last_k_idx-2): min_num += '0'
            min_num += '5'
            last_k_idx = idx
        idx += 1

    if last_k_idx != length -1:
        min_num += '1'
        idx -= 2
        while True:
            if idx == last_k_idx: break
            min_num += '0'
            idx -= 1
    return min_num

if __name__ == "__main__":
    main()