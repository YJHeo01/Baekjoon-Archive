#include <stdio.h>

int stack[100000] = { 0 };
int top = -1;
int main() {
	int n;
	int tmp;
	int command = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &command);
		switch (command)
		{
		case 1:
			scanf("%d", &tmp);
			stack[++top] = tmp;
			break;
		case 2:
			if (top > -1) {
				printf("%d\n", stack[top--]);
			}
			else {
				printf("-1\n");
			}
			break;
		case 3:
			printf("%d\n", top + 1);
			break;
		case 4:
			if (top == -1) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		case 5:
			if (top > -1)
			{
				printf("%d\n",stack[top]);
			}
			else {
				printf("-1\n");
			}
			break;
		default:
			break;
		}
	}
}