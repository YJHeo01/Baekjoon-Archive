#include <stdio.h>
#include <string.h>

int main()
{
	int a, b, c;
	scanf("%d",&a);
	scanf("%d", &b);
	scanf("%d", &c);
	unsigned int sum = a * b * c;
	int tmp = 0;
	int num[10] = {0};
	while (1) {
		if (sum == 0)
		{
			break;
		}
		tmp = sum % 10;
		sum = sum / 10;
		num[tmp] = num[tmp] + 1;
	}
	for (int i = 0; i <= 9; i++) {
		printf("%d\n", num[i]);
	}
}