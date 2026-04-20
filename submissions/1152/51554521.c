#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

char str[1000001];
int main()
{

    scanf("%[^\n]s", str);
    int cnt = 1;

    for (unsigned int i = 2; i <= (strlen(str)) - 1; i++)
    {
        if (str[i - 1] != ' ' && str[i] == ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}