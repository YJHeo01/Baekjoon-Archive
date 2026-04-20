#define MAX(a,b) (a > b) ? a : b;
#define MIN(a,b) (a < b) ? a : b;
#define SIZE 11
#include <stdio.h>

int num_list[SIZE] = { 0, };

int max_value = -1234567890;
int min_value = -max_value;
int n = 0;

void cal(int num_list[], int plus, int minus, int multi, int div, int idx, int sum_value) {
	if (idx >= n) {
		max_value = MAX(max_value, sum_value);
		min_value = MIN(min_value, sum_value);
		return;
	}
	if (plus != 0) {
		cal(num_list, plus-1, minus, multi, div, idx + 1, sum_value + num_list[idx]);
	}
	if (minus != 0) {
		cal(num_list, plus, minus-1, multi, div, idx + 1, sum_value - num_list[idx]);
	}
	if (multi != 0) {
		cal(num_list, plus, minus, multi-1, div, idx + 1, sum_value * num_list[idx]);
	}
	if (div != 0) {
		cal(num_list, plus, minus, multi, div-1, idx + 1, sum_value / num_list[idx]);
	}
}
int main()
{

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num_list[i]);
	}
	int plus, minus, multiple, div;
	scanf("%d %d %d %d", &plus, &minus, &multiple, &div);
	cal(num_list, plus, minus, multiple, div, 1, num_list[0]);
	printf("%d\n", max_value);
	printf("%d", min_value);
}