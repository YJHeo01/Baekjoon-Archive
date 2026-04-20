#include <stdio.h>
#include <math.h>

int main()
{
	char array[1001] = { 0 };
	array[1] = 1;
	int number[101] = { 0 };
	int max = 0;
	int n,j;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number[i]);
		if (max < number[i]) {
			max = number[i];
		}
	}
	int qrt = (int)sqrt(max);
	for (int i = 2; i <= qrt; i++) {
		if (array[i] == 0) {
			j = 2;
			while (i * j <= max) {
				array[i * j] = 1;
				j++;
			}
		}
	}
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (array[number[i]] == 0) {
			cnt++;
		}
	}
	printf("%d", cnt);
}