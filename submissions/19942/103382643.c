#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int compare(int a, int b) {
    int a_info[20] = { 0, };
    int b_info[20] = { 0, };
    memset(a_info, -1, sizeof(a_info));
    memset(b_info, -1, sizeof(b_info));
    int a_idx = 0;
    int b_idx = 0;
    for (int i = 0;i < 20;i++) {
        if ((1 << i) & a) {
            a_info[a_idx++] = i;
        }
        if ((1 << i) & b) {
            b_info[b_idx++] = i;
        }
    }
    for (int i = 0;i < 20;i++) {
        if (a_info[i] == b_info[i]) continue;
        if (a_info[i] > b_info) return 1;
        else return 0;
    }
    return 0;
}
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

        if (correct && (tmp[4] == answer_cost)) {
            if (compare(answer, state)) answer = state;
        }

        if (correct && (tmp[4] < answer_cost)) {
            answer = state;
            answer_cost = tmp[4];
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