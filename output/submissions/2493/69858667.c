#include <stdio.h>


int tower[500001] = { 0, };
int answer[500001] = { 0, };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &tower[i]);
		if (tower[i] < tower[i - 1]) {
			answer[i] = i - 1;
		}
		else if (tower[answer[i-1]]>tower[i]) {
			answer[i] = answer[i - 1];
		}
		else {
			for (int j = i-2; j >= 0; j--) {
				if (tower[answer[j]] > tower[i]) {
					answer[i] = answer[j];
					break;
				}
			}
		}
		printf("%d ", answer[i]);
	}
}