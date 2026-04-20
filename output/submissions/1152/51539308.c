#include <stdio.h>
#include <string.h>

char str[1000000];
int main()
{
 
    scanf("%[^\n]s", str);
    int cnt=1;
    
    for (int i = 1; i <= strlen(str); i++)
    {
        if (str[i - 1]!= ' ' && str[i] == ' ' && str[i+1] != ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt);
}