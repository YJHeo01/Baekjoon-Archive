#include <stdio.h>

int number_list[100000] = { 0, };

void sort(int n) {
	for (int i = n; i >= 1; i--) {
		if (number_list[i] < number_list[i - 1]) {
			int tmp = number_list[i];
			number_list[i] = number_list[i - 1];
			number_list[i - 1] = tmp;
		}
		else {
			return;
		}
	}
}
int main() {
	int n = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number_list[i]);
		sort(i);
		int mid = i / 2;
		printf("%d\n", number_list[mid]);
	}
}