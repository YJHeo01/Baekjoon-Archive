#include <stdio.h>

int sun_young[1000000] = { 0, };
int sang_keun[1000000] = { 0, };

int main() {
	while (1)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		if (n == 0 && m == 0) {
			break;
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &sang_keun[i]);
		}
		for (int i = 0; i < m; i++) {
			scanf("%d", &sun_young[i]);
		}
		int sang_keun_idx = 0;
		int sun_young_idx = 0;
		int answer = 0;
		while (1)
		{
			if (sang_keun_idx >= n || sun_young_idx >= m) {
				break;
			}
			if (sang_keun[sang_keun_idx] > sun_young[sun_young_idx]) {
				sun_young_idx += 1;
			}
			else if (sang_keun[sang_keun_idx] < sun_young[sun_young_idx]) {
				sang_keun_idx += 1;
			}
			else {
				answer++;
				sang_keun_idx++;
				sun_young_idx++;
			}
		}
		printf("%d\n", answer);
	}

}