#include <stdio.h>
#include <string.h>

char str[10000];
int main()
{
 
    scanf("%[^\n]s", str);
    int cnt=1;
    
    for (int i = 1; i <= (strlen(str))-2; i++)
    {
        if (str[i - 1]!= ' ' && str[i] == ' ' && str[i+1] != ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}