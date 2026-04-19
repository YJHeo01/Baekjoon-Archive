from itertools import permutations

def main():
    word_list = get_word_list()
    select_word = [False] * 6
    possible = backtracking(word_list,select_word,[])
    if possible == False: print(0)

def get_word_list():
    word_list = []
    for _ in range(6): word_list.append(list(input()))
    return word_list

def backtracking(word_list,select_word,row):
    if len(row) == 3:
        return create_test_case(word_list,select_word,row)
    ret_value = False
    for i in range(6):
        if select_word[i] == True: continue
        select_word[i] = True
        ret_value = backtracking(word_list,select_word,row+[i])
        select_word[i] = False
        if ret_value == True: break
    return ret_value

def create_test_case(word_list,select_word,rows):
    data = get_data(select_word)
    array = []
    for row in rows: array.append(word_list[row])
    columns = list(permutations(data,3))
    for column in columns:
        column = list(column)
        if check_correct_array(array,word_list,column) == True:
            print_answer(array)
            return True
    return False

def get_data(select_word):
    ret_value = []
    for i in range(6):
        if select_word[i] == False: ret_value.append(i)
    return ret_value

def check_correct_array(array,word_list,column):
    for i in range(3):
        for j in range(3):
            if array[i][j] != word_list[column[j]][i]: return False
    return True

def print_answer(array):
    for i in range(3):
        for j in range(3):
            print(array[i][j],end="")
        print()

if __name__ == "__main__":
    main()