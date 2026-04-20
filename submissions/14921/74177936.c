#include <stdio.h>
#include <stdlib.h>


int main() {
	int n;
	scanf("%d", &n);
	int value[100000] = { 0, };
	for (int i = 0; i < n; i++) {
		scanf("%d", &value[i]);
	}
	int left = 0;
	int right = n-1;
	int answer = 200000001;
	while (left < right) {
		int tmp = value[left] + value[right];
		if (abs(answer) > abs(tmp)) {
			answer = tmp;
		}
		if (tmp > 0) {
			right -= 1;
		}
		else
		{
			left += 1;
		}
	}
	printf("%d", answer);
}