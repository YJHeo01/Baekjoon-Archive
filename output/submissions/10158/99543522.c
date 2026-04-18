#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int w, h;
	int p, q;
	scanf("%d %d", &w, &h);
	scanf("%d %d", &p, &q);
	int t;
	scanf("%d", &t);
	int dx = t % (2*w);
	int dy = t % (2*h);
	if (p + dx > w) {
		dx -= (w - p);
		p = w;
		p -= dx;
		if (p < 0) p *= -1;
	}
	else p += dx;
	if (q + dy > h) {
		dy -= (h - q);
		q = h;
		q -= dy;
		if (q < 0) q *= -1;
	}
	else q += dy;
	printf("%d %d", p, q);
}