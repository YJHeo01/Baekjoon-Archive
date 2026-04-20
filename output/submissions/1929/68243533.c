#include <stdio.h>
#include <math.h>

int main()
{
    char array[1000001] = { 0 };
    int m, n, x;
    scanf("%d %d", &m, &n);
    x = (int)sqrt(n);
    for (int i = 2; i <= x; i++) {
        if (array[i] == 0) {
            int j = 2;
            while (i * j <= n) {
                array[i * j] = 1;
                j += 1;
            }
        }
    }
    for (int i = m; i <= n; i++) {
        if (array[i] == 0) {
            printf("%d\n", i);
        }
    }

}