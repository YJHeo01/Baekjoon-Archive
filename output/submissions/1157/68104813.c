int main()
{
	char c[1000000];
	scanf("%s", c);
	int alpha[26];
	for (int i = 0; i < strlen(c); i++)
	{
		if (c[i] >= 'a')
		{
			alpha[c[i] - 'a']++;
		}
		else {
			alpha[c[i] - 'A']++;
		}
	}
	char max = 0;
	int p = 0;
	for (int i = 1; i < 26; i++)
	{
		if (alpha[max] == alpha[i])
		{
			p = 1;
		}
		else if (alpha[max] < alpha[i]) {
			max = i;
			p = 0;
		}
	}
	if (p == 1) {
		printf("?");
	}
	else {
		max = max + 'A';
		printf("%C", max);
	}
}