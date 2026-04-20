#define _CRT_SECURE_NO_WARNINGS
#define SIZE 1000000
#include <stdio.h>

int num_list[SIZE] = { 0, };
int prefix_sum[SIZE + 1] = { 0, };
int main()
{
	int answer = 0;
	int sum = 0;

	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num_list[i]);
		sum += num_list[i];
		prefix_sum[i + 1] = sum;
		for (int j = 0; j < i + 1; j++) {
			if ((prefix_sum[i + 1] - prefix_sum[j]) % m == 0) {
				answer++;
			}
		}
	}
	printf("%d", answer);
}