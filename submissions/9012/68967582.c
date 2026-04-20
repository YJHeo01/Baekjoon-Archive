#include <stdio.h>
#include <string.h>

void print_yes_or_no(int i) {
	if (i == 1) {
		printf("YES\n");
	}
	else {
		printf("NO\n");
	}
	return;
}

void VPS(char str[]) {
	char index = -1;
	int l = strlen(str);
	for (int i = 0; i < l; i++) {
		if (str[i] == '(') {
			index++;
		}
		else {
			index--;
		}
		if (index < -1) {
			print_yes_or_no(0);
			return;
		}
	}
	if (index == -1) {
		print_yes_or_no(1);
		return;
	}
	print_yes_or_no(0);
	return;
}


int main() {
	int t;
	char str[50] = { 0, };
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%s", str);
        VPS(str);
	}
}