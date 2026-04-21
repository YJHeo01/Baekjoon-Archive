#include <stdio.h>
#include <string.h>

char str[1000001];
int main()
{

    scanf("%[^\n]s", str);
    int cnt = 1;

    if (str[0] == ' ')
    {
        cnt = 0;
        printf("0");
        return 0;
    }
    for (unsigned int i = 2; i <= (strlen(str)) - 1; i++)
    {
        if (str[i - 1] == ' ' && str[i] != ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}