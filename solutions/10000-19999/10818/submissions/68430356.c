#include <stdio.h>


int main()
{
	int max = -1000001;
	int min = 1000001;
	int n,tmp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		if (tmp < min) {
			min = tmp;
		}
		if (tmp > max) {
			max = tmp;
		}
	}
	printf("%d %d", min, max);
}