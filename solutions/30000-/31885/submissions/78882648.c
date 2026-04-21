#define MAX(a,b) a > b ? a : b
#define MAX_ITEM_CNT 200000
#include <stdio.h>

long long item[MAX_ITEM_CNT][2] = { 0, };

int n;
long long end_x,end_y;

int solution(long long x, long long y, int hp);

int main() {
	int k;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%lld %lld", &item[i][0], &item[i][1]);
	}
	scanf("%lld %lld", &end_x, &end_y);
	int answer = k - solution(0, 0, k);
	if (answer > k) answer = -1;
	printf("%d", answer);
}

int solution(long long x, long long y, int hp) {
	if (x == end_x && y == end_y) return hp;
	if (hp <= 0) return -1;
	int ret_value = -1;
	long long dx[4] = { 0,1,0,-1 };
	long long dy[4] = { 1,0,-1,0 };
	for (int i = 0; i < 4; i++) {
		long long nx = x + dx[i];
		long long ny = y + dy[i];
		ret_value = MAX(ret_value, solution(nx,ny,hp-1));
	}
	if (hp < 2) return ret_value;
	for (int i = 0; i < n; i++) {
		long long nx = x + item[i][0];
		long long ny = y + item[i][1];
		ret_value = MAX(ret_value, solution(nx, ny, hp - 2));
	}
	return ret_value;
}