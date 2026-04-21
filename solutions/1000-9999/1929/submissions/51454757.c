#include <stdio.h>

int main()
{
    int m, n, tmp;
    scanf_s("%d %d", &m, &n);
    for (int i = m; i <= n; i++)
    {
        tmp = 2;
        while (1)
        {
            
            if (tmp == i)
            {
                printf("%d\n", i);
                break;
            }

            if (i % tmp == 0)
            {
                break;
            }

            tmp++;
        }
    }
}