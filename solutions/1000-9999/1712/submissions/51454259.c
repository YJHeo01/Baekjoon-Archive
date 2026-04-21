#include <stdio.h>

int main()
{
    unsigned int a,b,c,cnt=0;
    scanf("%d %d %d",&a,&b,&c);
    if(b>c)
    {
        printf("-1");
        return;
    }
    while(1)
    {
        if(a+b*cnt < cnt*c)
        {
            break;
        }
        cnt++;
    }
    printf("%d",cnt);
}