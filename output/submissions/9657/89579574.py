n = int(input())

game = ['CY'] * 1001

game[1], game[3], game[4] = 'SK', 'SK', 'SK'

for i in range(5,n+1):
    for j in [1,3,4]:
        if game[i-j] == 'CY': game[i] = 'SK'
        
print(game[n])