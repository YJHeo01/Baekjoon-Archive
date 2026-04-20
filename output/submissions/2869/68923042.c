#include <stdio.h>
#include <math.h>
int main() {
	int a, b, v;
	scanf("%d %d %d", &a, &b, &v);
	v -= a;
	double cnt;
	cnt = ceil(v/(a-b)) + 1;
	

	printf("%d",(int)cnt);
	
}