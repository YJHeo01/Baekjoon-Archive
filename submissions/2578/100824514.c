#include <stdio.h>
#include <stdlib.h>

int arr[5][5] = { 0, };

int solution() {
    int answer = 0;
    int row_bingo[5] = { 0, };
    int cnt = 0;
    int column_bingo[5] = { 0, };
    int cross_bingo[2] = { 0, };
    while (1) {
        answer++;
        int tmp;
        scanf("%d", &tmp);
        for (int i = 0;i < 5;i++) {
            for (int j = 0;j < 5;j++) {
                if (arr[i][j] == tmp) arr[i][j] = 0;
            }
        }
        for (int i = 0;i < 5;i++) {
            if (row_bingo[i]) continue;
            int state = 1;
            for (int j = 0;j < 5;j++) {
                if (arr[i][j] != 0) state = 0;
            }
            if (state) {
                cnt++;
                row_bingo[i] = 1;
            }
        }
        for (int j = 0;j < 5;j++) {
            if (column_bingo[j]) continue;
            int state = 1;
            for (int i = 0;i < 5;i++) {
                if (arr[i][j] != 0) state = 0;
            }
            if (state) {
                cnt++;
                column_bingo[j] = 1;
            }
        }
        if (!cross_bingo[0]) {
            int state = 1;
            for (int i = 0;i < 5;i++) {
                if (arr[i][i] != 0) state = 0;
            }
            if (state) {
                cnt++;cross_bingo[0] = 1;
            }
        }
        if (!cross_bingo[1]) {
            int state = 1;
            for (int i = 0;i < 5;i++) {
                if (arr[i][4 - i] != 0) state = 0;
            }
            if (state) {
                cnt++;
                cross_bingo[1] = 1;
            }
        }
        if (cnt>=3) return answer;
    }
}
int main()
{
    for (int i = 0;i < 5;i++) {
        for (int j = 0;j < 5;j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    int answer = solution();
    printf("%d", answer);
    return 0;
}