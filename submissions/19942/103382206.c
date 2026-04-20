#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int n;
    scanf("%d", &n);

    int target[4] = { 0, };
    for (int i = 0;i < 4;i++) scanf("%d", &target[i]);

    int food[16][5] = { 0, };
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < 5;j++) {
            scanf("%d", &food[i][j]);
        }
    }

    int answer = 0;
    int answer_cost = 87654321;

    for (int state = 0;state < (1 << n);state++) {
        int tmp[5] = { 0, };
        for (int i = 0;i < n;i++) {
            if ((1 << i) & state) {
                for (int j = 0;j < 5;j++) {
                    tmp[j] += food[i][j];
                }
            }
        }
        bool correct = true;
        for (int i = 0;i < 4;i++) {
            if (tmp[i] < target[i]) correct = false;
        }
        if (correct && (tmp[4] < answer_cost)) {
            answer = state;
            answer_cost = tmp[4];
        }
        if (correct && tmp[4] == answer_cost) {
            for (int i = 0;i < n;i++) {
                if (((1 << i) & answer) != ((1 << i) & state)){
                    if (state & (1 << i)) answer = state;
                    break;
                }
            }
        }
    }

    if (answer == 0) printf("-1");
    else {
        printf("%d\n", answer_cost);
        for (int i = 0;i < n;i++) {
            if ((1 << i) & answer) printf("%d ", i+1);
        }
    }
    return 0;
}