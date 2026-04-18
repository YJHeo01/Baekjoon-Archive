int main() {
	char s[101] = { 0, };
	int answer[26] = { 0, };
	scanf("%s", s);
	for (int i = 0;i < 26;i++) answer[i] = -1;
	for (int i = 0;i < 100;i++) {
		if (s[i] == 0 || answer[s[i] - 'a'] != -1)break;
		answer[s[i] - 'a'] = i;
	}
	for (int i = 0;i < 26;i++) {
		printf("%d ", answer[i]);
	}
}