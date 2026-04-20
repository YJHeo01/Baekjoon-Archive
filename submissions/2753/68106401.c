#include <stdio.h>
#include <string.h>

int main()
{
	int year;
	int cnt = 0;
	scanf("%d", &year);
	if (year % 4 == 0) {
		if (year % 400 == 0) {
			cnt = 1;
		}
		else if (year % 100 != 0) {
			cnt = 1;
		}
	}
	printf("%d", cnt);
}