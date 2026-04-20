#include <stdio.h>

int main()
{
    int m, n, tmp;
    scanf("%d %d", &m, &n);
    for (int i = m; i <= n; i++)
    {
        tmp = 2;
        while (1)
        {
            


            if (i % tmp == 0)
            {
                if (tmp == i)
                {
                printf("%d\n", i);
                }
                break;
            }

            tmp++;
        }
    }
}