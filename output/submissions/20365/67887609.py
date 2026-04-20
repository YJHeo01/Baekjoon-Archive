n = int(input())

sentence = list(input())

red = sentence.count('R')
blue = n - red

if red>blue:
    print(blue+1)
else : print(red+1)