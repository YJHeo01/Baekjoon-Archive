#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char stack[100] = { 0, };
char last = 0;

int main()
{
	char string[100] = { 0, };
	while (scanf("%[\n]s", &string) != EOF) {
		int yes_no = 1;
		int l = strlen(string);
		for (int i = 0; i < l; i++) {
			switch (string[i]) {
			case '(':
				stack[last++] = '(';
				break;
			case ')':
				if (last <= 0 || stack[--last] == '[') {
					yes_no = 0;
				}
				break;
			case '[':
				stack[last++] = '[';
				break;
			case ']':
				if (last <= 0 || stack[--last] == '(') {
					yes_no = 0;
				}
				break;
			default:
				break;
			}
			if (yes_no == 0) {
				break;
			}
		}
		if (yes_no == 0) {
			printf("no");
		}
		else {
			printf("yes");
		}
		yes_no = 1;
		last = 0;
	}
}