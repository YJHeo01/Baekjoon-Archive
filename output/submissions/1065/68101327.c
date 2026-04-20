#include <stdio.h>


int main()
{
    int n,cnt,a1,a2,a3,tmp;
    scanf("%d", &n);

    if (n <= 99)
    {
        cnt = n;
    }
    else {
        cnt = 99;
        for (int i = 100; i <= n; i++)
        {
            tmp = i;
            a3 = tmp % 10;
            tmp -= a3;
            a2 = tmp % 100;
            tmp -= a2;
            a2 = a2 / 10;
            a1 = tmp / 100;
            if (a1 - a2 == a2 - a3)
            {
                cnt++;
            }
        }
    }
    printf("%d", cnt);
}