#define min(x,y) (x) < (y) ? (x) : (y)
#define max(x,y) (x) > (y) ? (x) : (y)
#include <stdio.h>


int main()
{
	int max_value = -1000001;
	int min_value = 1000001;
	int n,tmp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		min_value = min(tmp, min_value);
		max_value = max(tmp, max_value);
	}
	printf("%d %d", min_value, max_value);
}