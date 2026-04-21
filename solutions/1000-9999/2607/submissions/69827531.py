n = int(input())

word = []
original = list(input())
original_alpha = [0] * 26
original_length = len(original)
for w in original:
    original_alpha[ord(w)-ord('A')] += 1
answer = 0
for _ in range(n-1):
    compare_word = list(input())
    compare_word_length = len(compare_word)
    compare_word_alpha = [0] * 26
    for w in compare_word:
        compare_word_alpha[ord(w)-ord('A')] += 1
    not_same = 0
    one = 0
    if compare_word_length == original_length:
        for i in range(26):
            if compare_word_alpha[i] - original_alpha[i] == 0:
                continue
            elif abs(compare_word_alpha[i] - original_alpha[i]) == 1:
                one += 1
            else:
                not_same = 1
                break
            if one >= 3:
                not_same = 1
                break
    elif abs(compare_word_length-original_length) == 1:
        for i in range(26):
            if compare_word_alpha[i] - original_alpha[i] == 0:
                continue
            elif abs(compare_word_alpha[i] - original_alpha[i]) == 1:
                one += 1
            else:
                not_same = 1
                break
            if one >= 2:
                not_same = 1
                break
    else:
        not_same = 1
    if not_same == 0:
        answer += 1
print(answer)
