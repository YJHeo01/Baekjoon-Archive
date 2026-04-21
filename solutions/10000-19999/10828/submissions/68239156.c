#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int stack[10000] = { 0 };
int top = -1;

int main()
{
	char command[10000][20];
	int n = 0;
	int i = 0;
	scanf("%d", &n);
	char a;
	for (i = 0; i < n; i++) {
		scanf(" %[^\n]s\n", command[i]);
	}
	for (i = 0; i < n; i++) {
		a = command[i][0];
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
		case 'p':
			if (command[i][1] == 'u') {
				++top;
				stack[top] = 0;
				int cnt = 0;
				while (1)
				{
					stack[top] = stack[top] + (command[i][5+cnt] - 48);
					if (command[i][5+cnt+1] != '\0') {
						stack[top] = stack[top] * 10;
						cnt++;
					}
					else {
						break;
					}
				}
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