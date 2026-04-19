#include <stdio.h>
#include <string.h>

char str[1000001] = { 0, };

int main() {
	
	scanf("%s", str);
	int length = strlen(str);
	int cnt[26] = { 0, };

	for (int i = 0;i < length;i++) cnt[(str[i] | 32) - 'a']++;

	int answer_idx = 0;
	int same_cnt = 1;
	for (int i = 1;i < 26;i++) {
		if (cnt[answer_idx] == cnt[i]) same_cnt++;
		if (cnt[i] > cnt[answer_idx]) {
			same_cnt = 1;
			answer_idx = i;
		}
	}

	if (same_cnt >= 2)printf("?");
	else printf("%c", 'A' + answer_idx);

}
