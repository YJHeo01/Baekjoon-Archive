#include <stdio.h>

int main()
{
    int m, n, tmp;
    scanf("%d %d", &m, &n);
    if(m%2==0)
    {
        m = m+1;
    }
    for (int i = m; i <= n; i = i+2)
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