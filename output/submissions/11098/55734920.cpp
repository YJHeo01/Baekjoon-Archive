#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	char name[100][20];
	char name_tmp[20];
	int price[100] = {};
	int price_tmp = 0;
	int n=0;
	int p = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &p);
		for (int j = 0; j < p; j++)
		{
			scanf("%d %s", &price_tmp, name_tmp);
			if (price_tmp > price[i])
			{
				price[i] = price_tmp;
				for (int m = 0; m < 20; m++)
				{
					name[i][m] = name_tmp[m];
				}
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		printf("%d %s\n", price[i], name[i]);
	}
}