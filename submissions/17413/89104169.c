#include <stdio.h>
#include <stdbool.h>

char str[100001] = { 0, };

int main() {
	scanf("%[^\n]s", str);
	int length = strlen(str);
	bool word = true;
	int left = 0;
	for (int right = 0;right < length;right++) {
		if (word == false) {
			if (str[right] != '>') continue;
			for (int j = left;j <= right;j++) printf("%c", str[j]);
			word = true;
			left = right + 1;
		}
		else if (str[right] == ' ') {
			for (int j = right - 1;j >= left;j--) printf("%c", str[j]);
			printf(" ");
			left = right + 1;
		}
		else {
			if (str[right] != '<') continue;
			for (int j = right - 1;j >= left;j--) printf("%c", str[j]);
			word = false;
			left = right;
		}
	}
	if (word) { for (int i = length - 1;i >= left;i--) printf("%c", str[i]); }
	else { for (int i = left;i < length;i++) printf("%c", str[i]); }
}