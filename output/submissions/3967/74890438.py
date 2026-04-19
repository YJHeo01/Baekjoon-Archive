array = []

for _ in range(5):
    array.append(list(input()))

magic_star = [0] * 12
magic_star_position = []
idx = 0
use_alphabet = [False] * 12
for i in range(5):
    for j in range(9):
        if array[i][j] != '.':
            magic_star_position.append((i,j))
            magic_star[idx] = array[i][j]
            if magic_star[idx] != 'x':
                use_alphabet[ord(magic_star[idx]) - ord('A')] = True
            idx += 1

def check_magic_star_A(magic_star):
    sum_value = ord(magic_star[1]) + ord(magic_star[2]) + ord(magic_star[3]) + ord(magic_star[4]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def check_magic_star_B(magic_star):
    sum_value = ord(magic_star[0]) + ord(magic_star[2]) + ord(magic_star[5]) + ord(magic_star[7]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def check_magic_star_C(magic_star):
    sum_value = ord(magic_star[0]) + ord(magic_star[3]) + ord(magic_star[6]) + ord(magic_star[10]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def check_magic_star_D(magic_star):
    sum_value = ord(magic_star[7]) + ord(magic_star[8]) + ord(magic_star[9]) + ord(magic_star[10]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def check_magic_star_E(magic_star):
    sum_value = ord(magic_star[1]) + ord(magic_star[5]) + ord(magic_star[8]) + ord(magic_star[11]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def check_magic_star_F(magic_star):
    sum_value = ord(magic_star[4]) + ord(magic_star[6]) + ord(magic_star[9]) + ord(magic_star[11]) - 4*ord('A') + 4
    if sum_value == 26:
        return True
    else:
        return False

def make_magic_star(magic_star,use_alphabet,idx):
    if idx == 12:
        complete_make_magic_star = check_magic_star_E(magic_star) and check_magic_star_F(magic_star)
        return complete_make_magic_star
    elif idx == 5:
        check_magic_star = check_magic_star_A(magic_star)
        if check_magic_star == False:
            return False
    elif idx == 8:
        check_magic_star = check_magic_star_B(magic_star)
        if check_magic_star == False:
            return False
    elif idx == 11:
        check_magic_star = check_magic_star_C(magic_star) and check_magic_star_D(magic_star)
        if check_magic_star == False:
            return False
    if magic_star[idx] == 'x':
        for i in range(12):
            if use_alphabet[i] == False:
                use_alphabet[i] = True
                magic_star[idx] = chr(ord('A')+i)
                complete_make_magic_star = make_magic_star(magic_star,use_alphabet,idx+1)
                if complete_make_magic_star == True:
                    return True
                else:
                    use_alphabet[i] = False
                    magic_star[idx] = 'x'
        return False
    else:
        ret_value = make_magic_star(magic_star,use_alphabet,idx+1)
        return ret_value

make_magic_star(magic_star,use_alphabet,0)

idx = 0

for i in range(5):
    for j in range(9):
        if idx == 12 or magic_star_position[idx] != (i,j):
            print('.',end="")
        else:
            print(magic_star[idx],end="")
            idx += 1
    print()