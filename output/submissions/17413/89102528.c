#include <stdio.h>

char str[100001] = { 0, };

int main() {
	while (scanf("%s", str) != EOF) {
		int length = strlen(str);
		for (int i = length - 1;i >= 0;i--) {
			switch (str[i])
			{
			case '<':
				printf(">");
				break;
			case '>':
				printf("<");
				break;
			default:
				printf("%c", str[i]);
				break;
			}
		}
		printf(" ");
	}
}