#include <stdbool.h>
#include <stdio.h>

int main() {
	bool s[21] = { false, };
	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		char command[7] = { 0, };
		scanf("%s", &command);
		if (command[1] == 'l') {
			for (int x = 0; x <= 20; x++) s[x] = true;
			continue;
		}
		if (command[0] == 'e') {
			for (int x = 0; x <= 20; x++) s[x] = false;
			continue;
		}
		int x;
		scanf("%d", &x);
		switch (command[0])
		{
		case 'r':
			s[x] = false;
			break;
		case 'a':
			s[x] = true;
			break;
		case 't':
			if (s[x] == true) {
				s[x] = false;
			}
			else {
				s[x] = true;
			}
			break;
		default:
			if (s[x] == true) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		}
	}
}