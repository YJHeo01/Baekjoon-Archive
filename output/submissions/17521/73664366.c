#include <stdio.h>


int main() {
	long long int n;
	long long int coin_cnt = 0;
	long long int w;
	scanf("%lld %lld", &n, &w);
	long long int day_coin_value[15] = { 0, };
	for (int i = 0; i < n; i++) {
		scanf("%lld", &day_coin_value[i]);
	}
	for (int i = 0; i < (n - 1); i++) {
		if (day_coin_value[i] < day_coin_value[i + 1]) {
			coin_cnt += (w / day_coin_value[i]);
			w %= day_coin_value[i];
		}
		else {
			w += day_coin_value[i] * coin_cnt;
			coin_cnt = 0;
		}
	}
	w += (coin_cnt * day_coin_value[n - 1]);
	printf("%lld", w);
}