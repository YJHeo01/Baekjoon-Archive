#include <stdio.h>


int main()
{
	int n;
	int three = 0;
	int cnt = 0;
	int sum = 0;
	scanf("%d", &n);
	while (1) {
		if(n < 10){
			if (n % 3 == 0) {
				three = 1;
			}
			break;
		}
		cnt++;
		while (n > 0) {
			sum = sum + n % 10;
			n = n / 10;
		}
		n = sum;
		sum = 0;
	}
	printf("%d\n", cnt);
	if (three == 0) {
		printf("NO");
	}
	else {
		printf("TES");
	}
}