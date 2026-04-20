#include <stdio.h>

int stack[10000] = { 0 };
int top = -1;

int main()
{
	char command[7];
	int n = 0;
	int i = 0;
	scanf("%d", &n);
	char a;
	for (i = 0; i < n; i++) {
		scanf(" %[^\n]s\n", command);
		a = command[0];
		switch (a) {
		case 's':
			printf("%d\n", top + 1);
			break;
		case 'e':
			if (top == -1) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		case 't':
			if (top == -1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", stack[top]);
			}
			break;
		default:
			if (command[1] == 'u') {
				++top;
				stack[top] = command[5] - 48;
			}
			else {
				if (top != -1)
				{
					printf("%d\n", stack[top]);
					top--;
				}
				else {
					printf("-1\n");
				}
			}
		}

	}
}