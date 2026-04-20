#include <stdio.h>

int zero_count = 0;
int one_count = 0;

int fibonacci(int n) {
    if (n == 0) {
        zero_count++;
        return 0;
    } else if (n == 1) {
        one_count++;
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    while(1)
    {
        scanf("%d",&a);
        fibonacci(a);
        printf("%d %d\n",zero_count,one_count);
    }
}