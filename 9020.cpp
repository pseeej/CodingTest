#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		int n;
		scanf("%d", &n);

		int* arr = (int*)malloc(sizeof(int)*(n + 1));

		for (int i = 2; i <= n; i++)
			arr[i] = 1;

		arr[1] = 0;

		for (int i = 2; i <= n; i++)
			for (int j = 2; i*j <= n; j++) {
				arr[i*j] = 0;
			}

		int dist = 10000;
		int left = 0, right = 0;

		for (int i = 2; i <= n; i++) {
			if (arr[n - i] == 1 && arr[i] == 1) {
				if (dist > i - (n - i)) {
					left = i;
					right = n - i;
					dist = right - left;
				}
			}
			else;
		}
		printf("%d %d\n", left, right);
	}


	return 0;
}