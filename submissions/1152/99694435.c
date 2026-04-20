#include <stdio.h>

char a[1000005] = { 0, };

int main() {
    int ans = 1;

    gets(a);

    int l = 0;
    for (int i = 1;i < 1000000;i++)
    {
        if (a[i] == 0) break;
        if (a[i - 1] != ' ' && a[i] == ' ') ans++;
    }

    printf("%d", ans);

    return 0;
}