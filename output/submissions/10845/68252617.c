#include <stdio.h>
#include <stdlib.h>

int queue[10000] = { 0 };
int front = 0;
int end = -1;

int print_func(int front, int end, int a, int b) {
	if (end < front) {
		printf("%d\n", a);
	}
	else {
		printf("%d\n", b);
	}
}
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
			print_func(front, end, 1, 0);
			break;
		case 'f':
			print_func(front, end, -1, queue[front]);
			break;
		case 'b':
			print_func(front, end, -1, queue[end]);
			break;
		default:
			if (command[i][1] == 'o') {
				print_func(front, end, -1, queue[front]);
				if (end >= front) {
					front++;
				}
			}
			else {
				queue[++end] = atoi(command[i]+5);
			}

		}
	}
}