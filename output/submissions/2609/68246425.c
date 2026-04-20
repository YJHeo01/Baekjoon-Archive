#include <stdio.h>
#include <math.h>

int min_max_value(int* a, int *b) {
	if (a > b) {
		return 0;
	}
	else {
		int tmp = 0;
		tmp = *a;
		*a = *b;
		*b = tmp;
		return 0;
	}
}
int main()
{

	int n, m;
	scanf("%d %d", &n, &m);
	min_max_value(&n, &m);
	int tmp = m;
	int answer1, answer2;
	while (1) {
		if (n % tmp == 0 && m % tmp==0) {
			answer1 = tmp;
			break;
		}
		tmp--;
	}
	answer2 = n * m / tmp;
	printf("%d\n", answer1);
	printf("%d", answer2);
}