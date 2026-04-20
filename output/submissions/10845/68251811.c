#include <stdio.h>
#include <stdlib.h>

int queue[10000] = { 0 };
int front = 0;
int end = -1;

int main() {
	int n;
	scanf("%d", &n);
	char command[10000][13];
	for (int i = 0; i < n; i++) {
		scanf(" %[^\n]s", command[i]);
	}
	for (int i = 0; i < n; i++) {
		switch (command[i][0]) {
		case 's':
			printf("%d\n", end - front + 1);
			break;
		case 'e':
			if (end < front) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		case 'f':
			if (end < front) {
				printf("-1\n");
			}
			else {
				printf("%d\n", queue[front]);
			}
			break;
		case 'b':
			if (end < front) {
				printf("-1\n");
			}
			else {
				printf("%d\n", queue[end]);
			}
			break;
		default:
			if (command[i][1] == 'o') {
				if (end < front) {
					printf("-1\n");
				}
				else {
					printf("%d\n", queue[front]);
					front++;
				}
			}
			else {
				queue[++end] = atoi(command[i]+5);
			}

		}
	}
}