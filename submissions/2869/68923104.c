#include <stdio.h>
#include <math.h>
int main() {
	double a, b, v;
	scanf("%lf %lf %lf", &a, &b, &v);
	v -= a;
	double cnt;
	cnt = ceil(v/(a-b)) + 1;
	

	printf("%d",(int)cnt);
	
}