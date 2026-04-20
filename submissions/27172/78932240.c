#include <stdio.h>

int card[100000] = { 0, };
int score[100000] = { 0, };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &card[i]);
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (card[i] % card[j] == 0) {
				score[j]++;
				score[i]--;
			}
			else if (card[j] % card[i] == 0) {
				score[i]++;
				score[j]--;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", score[i]);
	}
}