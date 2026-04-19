import math

def main():
    for _ in range(int(input())):
        tmp = list(map(float,input().split()))
        first_player_score, second_player_score = 0,0
        for i in range(0,6,2):
            x,y = tmp[i], tmp[i+1]
            distance = math.sqrt(x**2+y**2)
            first_player_score += change_score(distance)
        for i in range(6,12,2):
            x,y = tmp[i], tmp[i+1]
            distance = math.sqrt(x**2+y**2)
            second_player_score += change_score(distance)
        print("SCORE: " +str(first_player_score) + " to " + str(second_player_score),end=", ")
        if first_player_score > second_player_score:
            print("PLAYER 1 WINS.")
        elif first_player_score < second_player_score:
            print("PLAYER 2 WINS.")
        else:
            print("TIE.")

def change_score(distance):
    if distance <= 3:
        return 100
    elif distance <= 6:
        return 80
    elif distance <= 9:
        return 60
    elif distance <= 12:
        return 40
    elif distance <= 15:
        return 20
    else:
        return 0
    return 0

if __name__ == "__main__":
    main()