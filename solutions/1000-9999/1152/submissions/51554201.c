#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main()
{
    char str[1000001];
    scanf("%[^\n]s", str);
    int cnt = 1;

    for (unsigned int i = 1; i <= (strlen(str)) - 2; i++)
    {
        if (str[i - 1] != ' ' && str[i] == ' ' && str[i + 1] != ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}