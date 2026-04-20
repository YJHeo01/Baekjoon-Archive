#include <stdio.h>

int main()
{
    int n, a, b, c, d, e, f, g, h;
    scanf("%d %d %d %d %d %d %d %d %d", &n, &a, &b, &c, &d, &e, &f, &g, &h);
    int cnt = 0;
    int x, y, z;
    for (int i = 0;i <= n;i++) {
        for (int j = 0;j <= (n - i);j++) {
            int k = n - i - j;
            if (a * i + b * j + c * k != d) continue;
            if (e * i + f * j + g * k != h)continue;
            cnt++;
            x = i;
            y = j;
            z = k;
        }
    }
    if (cnt == 1) cnt = 0;
    else if (cnt == 0)cnt = 2;
    else cnt = 1;

    printf("%d\n", cnt);
    if (cnt == 0) printf("%d %d %d", x, y, z);
    return 0;
}