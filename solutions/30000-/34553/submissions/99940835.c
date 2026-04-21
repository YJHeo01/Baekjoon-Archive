#include <stdio.h>

int main(void)
{
    char S[100001] = { 0, };
    scanf("%s", S);
    char* ptr;
    int temp;
    int answer;
    
    temp = 1;
    answer = 1;

    ptr = S + 1;
    while (1) {
        if (*ptr == 0) break;
        if (*ptr > *(ptr - 1)) temp++;
        else temp = 1;
        answer += temp;
        ptr = ptr + 1;
    }

    printf("%d", answer);
    return 0;
}