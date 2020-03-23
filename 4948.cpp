#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {

	int n;

	scanf("%d", &n);

	while (n != 0) {
		int* arr = (int*)malloc(sizeof(int)*(n + n + 1));
		for (int i = 2; i <= n+n; i++)
			arr[i] = 1;

		for (int i = 2; i <= sqrt(n+n); i++)
			if (arr[i] == 1) {
				for (int j = i+i; j <= n + n;j+=i) {
					if (arr[j] == 1)
						arr[j] = 0;
				}
			}

		int count = 0;

		for (int i = n+1; i <= n + n; i++) {
			if (arr[i] == 1)
				count++;
		}

		printf("%d\n", count);

		free(arr);

		scanf("%d", &n);
	}

	return 0;
}