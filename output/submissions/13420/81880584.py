n = int(input())
for _ in range(n):
    a, icon, b, tmp, c = input().split()
    a,b,c = int(a), int(b), int(c)
    correct = True
    if icon == '*':
        if a * b != c: correct = False
    elif icon == '/':
        if a // b != c: correct = False
    elif icon == '+':
        if a + b != c: correct = False
    else:
        if a - b != c: correct = False
    if correct == True:
        print("correct")
    else:
        print("wrong answer")